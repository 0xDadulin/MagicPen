import openai
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import os
from collections import defaultdict
from .models import UlepszonyTekst
from .forms import UlepszonyTekstForm
from dotenv import load_dotenv
from .prompts import get_prompt
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objs as go
from django.utils import timezone
from django.db.models import Sum
from django.db.models.functions import TruncDate
from collections import namedtuple, Counter


load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
openai.api_key = os.environ['openai']


@login_required  # Wymaga zalogowania przed dostępem do tej funkcji
def generuj_opis(request):
    ulepszony_tekst = 'test'  # Domyślny tekst na początku

    # Sprawdzenie czy metoda żądania to POST
    if request.method == 'POST':
        # Utworzenie formularza na podstawie przesłanych danych POST
        form = UlepszonyTekstForm(request.POST, initial=request.POST)
        # Sprawdzenie czy dane w formularzu są poprawne
        if form.is_valid():
            # Wyodrębnienie danych z poprawionego formularza
            ton = form.cleaned_data['ton']
            zastosowanie = form.cleaned_data['zastosowanie']
            tekst = form.cleaned_data['tekst']
            # Pobieranie odpowiedniego wprowadzenia do pytania na podstawie zastosowania
            system_prompt = get_prompt(zastosowanie)

            # Ulepszanie tekstu przy użyciu funkcji i przypisanie wyników do zmiennych
            ulepszony_tekst, tokens = ulepsz_opis(ton, tekst, system_prompt)
            # Liczenie słów w ulepszonym tekście
            liczba_slow = len(ulepszony_tekst.split())

            # Utworzenie nowego obiektu modelu z danymi
            ulepszony_tekst_model = UlepszonyTekst(
                uzytkownik=request.user,
                ton=ton,
                zastosowanie=zastosowanie,
                tekst=tekst,
                ulepszony_tekst=ulepszony_tekst,
                tokens=tokens,
                liczba_slow=liczba_slow,
                created_at=timezone.now(),
            )
            # Zapisanie obiektu modelu do bazy danych
            ulepszony_tekst_model.save()

            # Konwersja obiektu modelu na słownik, a następnie na odpowiedź JSON
            ulepszony_tekst_dict = model_to_dict(ulepszony_tekst_model)
            return JsonResponse(ulepszony_tekst_dict)
        else:
            # Odpowiedź w przypadku niepoprawnych danych formularza
            return HttpResponse('Błąd formularza', status=400)

    # Tworzenie nowego, pustego formularza w przypadku innej metody niż POST
    form = UlepszonyTekstForm()

    # Renderowanie strony z formularzem
    return render(request, 'index.html', context={'form': form, 'ulepszony': ulepszony_tekst})

def ulepsz_opis(ton, tekst, system_prompt):
    # Przygotowanie treści do przesłania do API OpenAI
    prompt = f"zastosuj taki ton odpowiedzi -> {ton}. Treść zapytania: {tekst}"
    # Wysłanie zapytania do modelu GPT-3.5 OpenAI z odpowiednimi danymi
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": system_prompt},
            {"role": "user",
             "content": tekst}
        ]
    )
    # Wyodrębnienie odpowiedzi modelu i liczby użytych tokenów
    opis = response['choices'][0]['message']['content']
    tokens = response['usage']['total_tokens']
    return opis, tokens  # Zwrócenie ulepszonego opisu i liczby tokenów

def signup(request):
  # Sprawdzanie czy metoda żądania to POST
  if request.method == 'POST':
      # Utworzenie formularza rejestracji na podstawie przesłanych danych POST
      form = UserCreationForm(request.POST)
      # Sprawdzenie czy dane w formularzu są poprawne
      if form.is_valid():
          # Zapisanie użytkownika i zwrócenie obiektu user
          user = form.save()
          # Logowanie nowo utworzonego użytkownika
          login(request, user)
          # Przekierowanie na stronę główną
          return redirect('landing')
  else:
      # Tworzenie nowego, pustego formularza rejestracji w przypadku innej metody niż POST
      form = UserCreationForm()

  # Renderowanie strony rejestracji z formularzem
  return render(request, 'signup.html', {'form': form})

def login_view(request):
  # Sprawdzanie czy metoda żądania to POST
  if request.method == 'POST':
      # Utworzenie formularza logowania na podstawie przesłanych danych POST
      form = AuthenticationForm(data=request.POST)
      # Sprawdzenie czy dane w formularzu są poprawne
      if form.is_valid():
          # Pobranie użytkownika na podstawie danych w formularzu
          user = form.get_user()
          # Logowanie użytkownika
          login(request, user)
          # Przekierowanie na stronę generowania opisu
          return redirect('generuj-opis')
  else:
      # Tworzenie nowego, pustego formularza logowania w przypadku innej metody niż POST
      form = AuthenticationForm()

  # Renderowanie strony logowania z formularzem
  return render(request, 'login.html', {'form': form})

def logout_view(request):
  # Wylogowanie użytkownika
  logout(request)
  # Przekierowanie na stronę generowania opisu
  return redirect('landing')

@login_required  # Wymaga zalogowania przed dostępem do tej funkcji
@csrf_exempt  # Wyłącza ochronę CSRF dla tej funkcji
def toggle_ulubiony(request, pk):
    # Sprawdzanie czy metoda żądania to POST
    if request.method == 'POST':
        # Pobranie obiektu UlepszonyTekst na podstawie przekazanego klucza głównego (pk)
        tekst = UlepszonyTekst.objects.get(pk=pk)
        # Zmiana stanu pola ulubiony na przeciwny
        tekst.ulubiony = not tekst.ulubiony
        # Zapisanie zmian w obiekcie
        tekst.save()
        # Zwrócenie odpowiedzi o sukcesie
        return HttpResponse('success')
    else:
        # Zwrócenie błędu w przypadku innej metody niż POST
        return HttpResponse('error', status=400)

@login_required  # Wymaga zalogowania przed dostępem do tej funkcji
@csrf_exempt  # Wyłącza ochronę CSRF dla tej funkcji
def aktualizuj_opis(request, pk):
    # Sprawdzanie czy metoda żądania to POST
    if request.method == 'POST':
        try:
            # Pobranie obiektu UlepszonyTekst na podstawie przekazanego klucza głównego (pk) i aktualnie zalogowanego użytkownika
            ulepszony_tekst = UlepszonyTekst.objects.get(pk=pk, uzytkownik=request.user)
            # Aktualizacja pola ulepszony_tekst na podstawie przesłanych danych POST
            ulepszony_tekst.ulepszony_tekst = request.POST['ulepszony_tekst']
            # Zapisanie zmian w obiekcie
            ulepszony_tekst.save()
            # Zwrócenie odpowiedzi o sukcesie w formacie JSON
            return JsonResponse({'status': 'success'})
        except UlepszonyTekst.DoesNotExist:
            # Zwrócenie błędu w przypadku braku obiektu UlepszonyTekst
            return JsonResponse({'status': 'error'}, status=404)
    else:
        # Zwrócenie błędu w przypadku innej metody niż POST
        return JsonResponse({'status': 'error'}, status=405)

def profil(request):
  # Pobranie tekstów użytkownika z ostatnich 30 dni
  data_od = timezone.now() - timedelta(days=30)
  data_do = timezone.now()
  teksty_uzytkownika = UlepszonyTekst.objects.filter(uzytkownik=request.user, created_at__range=(data_od, data_do))

  # Agregacja danych tekstów użytkownika według daty oraz obliczenie sumy słów dla każdego dnia
  grouped_data = teksty_uzytkownika.annotate(day=TruncDate('created_at')).values('day').annotate(sum_words=Sum('liczba_slow')).order_by('day')

  # Inicjalizacja domyślnych danych dla ostatnich 30 dni z zerową liczbą słów
  daily_data = defaultdict(int)
  for i in range(30):
      day = (timezone.now() - timedelta(days=i)).date()
      daily_data[day] = 0

  # Aktualizacja danych na podstawie zgrupowanych wyników z bazy danych
  for record in grouped_data:
      daily_data[record['day']] = record['sum_words']

  # Tworzenie wykresu słupkowego przedstawiającego zużycie słów przez użytkownika w ciągu ostatnich 30 dni
  data = go.Bar(
      x=list(daily_data.keys()),
      y=list(daily_data.values()),
      text=[f"Zużycie: {v}" for v in daily_data.values()],
      hovertemplate="%{text}<br>%{x}",
      name=""
  )
  layout = go.Layout(title="Zużycie słów przez użytkownika w ostatnich 30 dniach", xaxis=dict(title="Data"), yaxis=dict(title=""))
  fig = go.Figure(data=[data], layout=layout)
  div = plot(fig, output_type='div', include_plotlyjs=False)

  # Gromadzenie statystyk na temat użycia różnych zastosowań
  Usage = namedtuple('Usage', ['name', 'count'])
  zastosowania = UlepszonyTekst.objects.values_list('zastosowanie', flat=True)
  zastosowania_count = Counter(zastosowania)
  usages = []

  # Tworzenie listy nazw zastosowań i ich liczby wystąpień
  for choice, choice_name in UlepszonyTekst._meta.get_field('zastosowanie').choices:
      usages.append(Usage(name=choice_name, count=zastosowania_count.get(choice, 0)))

  # Sortowanie listy usages w kolejności malejącej na podstawie liczby wystąpień
  usages = sorted(usages, key=lambda x: x.count, reverse=True)

  # Obliczanie łącznej liczby słów i oszacowanie zaoszczędzonego czasu oraz pieniędzy
  liczba_slow = UlepszonyTekst.objects.filter(uzytkownik=request.user).aggregate(Sum('liczba_slow'))['liczba_slow__sum'] or 0
  zaoszczedzony_czas = round((liczba_slow / 1000) * 60, 2)  # Zakładając, że 1000 słów = 60 minut
  zaoszczedzone_pieniadze = round(zaoszczedzony_czas * 20, 2)  # Zakładając stawkę 20 jednostek waluty za godzinę

  # Renderowanie strony profilu z wykresem oraz statystykami
  return render(request, 'profil.html', {'wykres': div, 'usages': usages, 'zaoszczedzony_czas': zaoszczedzony_czas,
                                         'zaoszczedzone_pieniadze': zaoszczedzone_pieniadze})

def landing(request):
  return render(request,'landing.html')
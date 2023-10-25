from django.shortcuts import render, redirect, get_object_or_404
from hr_helper.models import UlepszonyTekst
from .forms import UlepszonyTekstForm

# Listowanie ulepszonych tekstów
def ulepszony_tekst_list(request):
    # Pobieranie wszystkich ulepszonych tekstów dla zalogowanego użytkownika
    ulepszone_teksty = UlepszonyTekst.objects.filter(uzytkownik=request.user)

    # Renderowanie listy ulepszonych tekstów
    return render(request, 'ulepszony_tekst_list.html', {'ulepszone_teksty': ulepszone_teksty})

# Strona szczegółów ulepszonych tekstów
def ulepszony_tekst_detail(request, tekst_id):
    # Pobieranie szczegółów konkretnego ulepszonych tekstu na podstawie jego ID oraz użytkownika
    ulepszony_tekst = get_object_or_404(UlepszonyTekst, id=tekst_id, uzytkownik=request.user)

    # Renderowanie strony szczegółów ulepszonych tekstu
    return render(request, 'ulepszony_tekst.html', {'ulepszony_tekst': ulepszony_tekst})

# Edycja istniejącego ulepszonych tekstów
def ulepszony_tekst_update(request, tekst_id):
    # Pobieranie istniejącego ulepszonych tekstu na podstawie jego ID oraz użytkownika
    ulepszony_tekst = get_object_or_404(UlepszonyTekst, id=tekst_id, uzytkownik=request.user)

    # Jeśli metoda żądania to POST (przesyłanie danych formularza)
    if request.method == 'POST':
        # Tworzenie formularza z danymi POST oraz instancją ulepszonych tekstu do aktualizacji
        form = UlepszonyTekstForm(request.POST, instance=ulepszony_tekst)

        # Sprawdzanie, czy dane w formularzu są poprawne
        if form.is_valid():
            # Zapisywanie aktualizacji ulepszonych tekstu
            form.save()
            # Przekierowywanie użytkownika do strony szczegółów tego ulepszonych tekstu
            return redirect('ulepszony_tekst_detail', tekst_id=ulepszony_tekst.id)
    # Jeśli metoda żądania to nie POST (np. GET)
    else:
        # Tworzenie formularza z instancją ulepszonych tekstu do edycji (bez danych POST)
        form = UlepszonyTekstForm(instance=ulepszony_tekst)

    # Renderowanie strony formularza edycji ulepszonych tekstu
    return render(request, 'ulepszony_tekst_form.html', {'form': form, 'ulepszony_tekst': ulepszony_tekst})

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import make_aware
from django.utils import timezone



class UlepszonyTekst(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    ton = models.CharField(max_length=255, choices=[
        ('optymistyczny', '😊 Optymistyczny'),
        ('neutralny', '😐 Neutralny'),
        ('poważny', '🧐 Poważny'),
        ('wesoły', '😄 Wesoły'),
        ('inspirujący', '💡 Inspirujący'),
        ('przyjacielski', '🤗 Przyjacielski'),
        ('formalny', '👔 Formalny'),
        ('ironiczny', '🙃 Ironiczny'),
        ('krytyczny', '🔍 Krytyczny'),
        ('żartobliwy', '😜 Żartobliwy'),
        ('nostalgiczny', '🕰️ Nostalgiczny'),
        ('romantyczny', '💖 Romantyczny'),
        ('sarkastyczny', '😏 Sarkastyczny'),
    ])
    zastosowanie = models.CharField(max_length=255, choices=[
        ('opis_produktu', '📦 Opis produktu'),
        ('artykul', '📝 Artykuł'),
        ('recenzja', '🌟 Recenzja'),
        ('pomysly_na_artykul', '💡 Pomysły na artykuł na bloga'),
        ('nazwa_dla_firmy', '🏢 Nazwa dla firmy/projektu'),
        ('pomysly_na_firme', '🚀 Pomysły na firmę'),
        ('wezwanie_do_dzialania', '✊ Wezwanie do działania'),
        ('list_motywacyjny', '📄 List motywacyjny'),
        ('email', '📧 Email'),
        ('reklama', '📣 Reklama na FB, IG, LinkedIn itp.'),
        ('pytania_do_wywiadu', '❓ Pytania do wywiadu'),
        ('opis_oferty_pracy', '🔍 Opis oferty pracy'),
        ('generator_slow_kluczowych', '🔖 Generator słów kluczowych/tagów'),
        ('pomysly_na_posty', '📲 Pomysły na posty na social media'),
        ('opis_profilu', '👤 Opis profilu (bio)'),
        ('pytania_i_odpowiedzi', '💬 Pytania i odpowiedzi (Q&A)'),
        ('odpowiedz_na_recenzje', '💼 Odpowiedz na recenzje/wiadomości'),
        ('seo_meta_tytul', '🔎 SEO meta tytuł'),
        ('seo_meta_opis', '📈 SEO meta opis'),
        ('tekst_piosenki', '🎤 Tekst piosenki'),
        ('zaswiadczenie', '📄 Zaświadczenie/recenzja'),
        ('yt_opis_kanalu', '📺 YT - opis kanału'),
        ('yt_opis_filmu', '🎬 YT - opis filmu'),
        ('yt_pomysly_na_film', '🎥 YT - pomysły na film'),
    ])
    tekst = models.TextField()
    ulepszony_tekst = RichTextField()
    created_at = models.DateTimeField(default=timezone.now)
    ulubiony = models.BooleanField(default=False)
    tokens = models.IntegerField(blank=True, null=True)
    liczba_slow = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.ton} - {self.zastosowanie} - {self.tekst[:50]} - {self.liczba_slow}"


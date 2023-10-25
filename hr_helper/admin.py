
from django.contrib.auth.admin import UserAdmin
from .models import UlepszonyTekst

from django.contrib import admin

class UlepszonyTekstAdmin(admin.ModelAdmin):
    list_display = ('uzytkownik', 'ton', 'zastosowanie', 'tekst', 'created_at', 'liczba_slow')
    list_filter = ('uzytkownik', 'ton', 'zastosowanie', 'created_at')
    search_fields = ('tekst', 'ulepszony_tekst')

admin.site.register(UlepszonyTekst, UlepszonyTekstAdmin)
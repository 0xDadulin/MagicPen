from django import forms
from hr_helper.models import UlepszonyTekst

class UlepszonyTekstForm(forms.ModelForm):
    class Meta:
        model = UlepszonyTekst
        fields = ['ulepszony_tekst']
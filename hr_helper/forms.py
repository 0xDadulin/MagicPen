from django import forms
from .models import UlepszonyTekst
from django.utils.safestring import mark_safe

class ZastosowanieInfoWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return mark_safe('<div id="zastosowanie-info" class="form-text"></div>')

class UlepszonyTekstForm(forms.ModelForm):
    zastosowanie_info = forms.CharField(required=False, widget=ZastosowanieInfoWidget())

    class Meta:
        model = UlepszonyTekst
        fields = ['ton', 'zastosowanie', 'tekst', 'zastosowanie_info']
        labels = {
            'ton': 'Ton',
            'zastosowanie': 'Zastosowanie',
            'tekst': 'Tekst',
            'zastosowanie_info': '',
        }
        widgets = {
            'ton': forms.Select(attrs={'class': 'form-select'}),
            'zastosowanie': forms.Select(attrs={'class': 'form-select', 'id': 'zastosowanie-select'}),
            'tekst': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

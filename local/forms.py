from django import forms
from .models import LocalEsportivo, Usuario

class LocalEsportivoForm(forms.ModelForm):
    # Alteração do campo anfitriao para ser um select com os anfitriões
    anfitriao = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(tipo_usuario=Usuario.ANFITRIAO),  # Filtrando os anfitriões
        required=True,
        empty_label="Escolha um anfitrião",  # Valor padrão para o select
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = LocalEsportivo
        fields = ['nome', 'endereco', 'capacidade', 'anfitriao', 'latitude', 'longitude']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_latitude(self):
        latitude = self.cleaned_data['latitude']
        if latitude:
            latitude = str(latitude).replace(',', '.')
        return float(latitude) if latitude else None

    def clean_longitude(self):
        longitude = self.cleaned_data['longitude']
        if longitude:
            longitude = str(longitude).replace(',', '.')
        return float(longitude) if longitude else None

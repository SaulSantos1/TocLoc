from django import forms
from .models import Disponibilidade
from django.utils.timezone import now

class DisponibilidadeForm(forms.ModelForm):
    class Meta:
        model = Disponibilidade
        fields = ['local', 'data', 'horario_inicio', 'horario_fim']
        widgets = {
            'local': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}, 
                format='%Y-%m-%d'
            ),
            'horario_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'horario_fim': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Define o valor inicial padrão para a data como o dia atual
        if not self.instance.pk:  # Se for uma nova instância
            self.fields['data'].initial = now().date()

    def clean(self):
        cleaned_data = super().clean()
        horario_inicio = cleaned_data.get('horario_inicio')
        horario_fim = cleaned_data.get('horario_fim')

        if horario_inicio and horario_fim and horario_inicio >= horario_fim:
            raise forms.ValidationError("O horário de início deve ser menor que o horário de fim.")
        return cleaned_data

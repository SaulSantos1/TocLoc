from django import forms
from .models import Reserva
from disponibilidade.models import Disponibilidade

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['local', 'usuario' ,'data', 'horario_inicio', 'horario_fim']
        widgets = {
            'local': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'horario_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'horario_fim': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'local' in self.data and 'data' in self.data:
            local = self.data.get('local')
            data = self.data.get('data')

            # Filtrar disponibilidades com base no local e data
            disponibilidades = Disponibilidade.objects.filter(local=local, data=data)
            horarios_disponiveis = []

            for disponibilidade in disponibilidades:
                horarios_disponiveis += self._gerar_opcoes_horarios(
                    disponibilidade.horario_inicio,
                    disponibilidade.horario_fim
                )

            # Definir opções no campo 'horario_inicio'
            self.fields['horario_inicio'].widget.choices = [(h, h) for h in sorted(set(horarios_disponiveis))]

    def _gerar_opcoes_horarios(self, horario_inicio, horario_fim):
        """
        Gera uma lista de horários disponíveis de 30 em 30 minutos entre um intervalo.
        """
        from datetime import timedelta, datetime

        horarios = []
        atual = datetime.combine(datetime.today(), horario_inicio)
        fim = datetime.combine(datetime.today(), horario_fim)

        while atual < fim:
            horarios.append(atual.time())
            atual += timedelta(minutes=30)  # Intervalos de 30 minutos

        return horarios

    def clean(self):
        cleaned_data = super().clean()
        local = cleaned_data.get('local')
        data = cleaned_data.get('data')
        horario_inicio = cleaned_data.get('horario_inicio')
        horario_fim = cleaned_data.get('horario_fim')

        if horario_inicio and horario_fim and horario_inicio >= horario_fim:
            raise forms.ValidationError("O horário de início deve ser menor que o horário de fim.")

        # Verificar se a reserva está dentro da disponibilidade do local
        disponibilidade = Disponibilidade.objects.filter(
            local=local,
            data=data,
        ).first()

        if disponibilidade:
            if not (disponibilidade.horario_inicio <= horario_inicio < disponibilidade.horario_fim):
                raise forms.ValidationError("O horário de início não está dentro da disponibilidade do local.")
            if not (disponibilidade.horario_inicio < horario_fim <= disponibilidade.horario_fim):
                raise forms.ValidationError("O horário de fim não está dentro da disponibilidade do local.")
        else:
            raise forms.ValidationError("Não há disponibilidade para o local na data selecionada.")

        return cleaned_data

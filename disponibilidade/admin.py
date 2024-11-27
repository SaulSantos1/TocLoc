from django.contrib import admin
from .models import Disponibilidade

@admin.register(Disponibilidade)
class DisponibilidadeAdmin(admin.ModelAdmin):
    list_display = ('local', 'data', 'horario_inicio', 'horario_fim')  # Campos exibidos na lista
    list_filter = ('local', 'data')  # Filtros laterais para locais e datas
    search_fields = ('local__nome',)  # Campo de busca baseado no nome do local
    ordering = ('data', 'horario_inicio')  # Ordenação por data e horário de início
    date_hierarchy = 'data'  # Hierarquia para navegação por datas

    fieldsets = (
        (None, {
            'fields': ('local', 'data', 'horario_inicio', 'horario_fim')
        }),
    )

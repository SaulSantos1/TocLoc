from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('local', 'usuario', 'data', 'horario_inicio', 'horario_fim')
    list_filter = ('local', 'data')  # Filtros para facilitar a navegação
    search_fields = ('local__nome', 'usuario__username')  # Campos de pesquisa
    ordering = ('data', 'horario_inicio')  # Ordenação padrão
    date_hierarchy = 'data'  # Hierarquia de datas para fácil navegação

    # Campos para edição e visualização detalhada
    fieldsets = (
        (None, {
            'fields': ('local', 'usuario', 'data', 'horario_inicio', 'horario_fim')
        }),
    )

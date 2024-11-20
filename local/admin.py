from django.contrib import admin
from django.db import models
from .models import LocalEsportivo

class LocalEsportivoAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na lista de objetos
    list_display = ('nome', 'endereco', 'capacidade', 'anfitriao', 'latitude', 'longitude')

    # Campos que podem ser filtrados na barra lateral do admin
    list_filter = ('anfitriao', 'capacidade')

    # Campos para busca no admin
    search_fields = ('nome', 'endereco')

    # Campos que serão editáveis diretamente na lista (inline)
    list_editable = ('latitude', 'longitude')

    # Definir o formato de exibição dos campos no formulário de edição
    fieldsets = (
        (None, {
            'fields': ('nome', 'endereco', 'capacidade', 'anfitriao')
        }),
        ('Localização', {
            'fields': ('latitude', 'longitude'),
            'classes': ('collapse',),  # Oculta a seção de localização por padrão
        }),
    )

    # Definir quais campos aparecem ao adicionar/editar o objeto
    formfield_overrides = {
        models.FloatField: {'widget': admin.widgets.AdminTextInputWidget},
    }

# Registra o modelo no admin
admin.site.register(LocalEsportivo, LocalEsportivoAdmin)

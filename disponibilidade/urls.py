from django.urls import path
from . import views

urlpatterns = [
    # URL para listar todas as disponibilidades
    path('disponibilidades/', views.listar_disponibilidades, name='listar_disponibilidades'),

    # URL para criar ou editar uma disponibilidade
    path('disponibilidade/editar/<int:disponibilidade_id>/', views.criar_editar_disponibilidade, name='criar_editar_disponibilidade'),

    # URL para criar uma nova disponibilidade
    path('disponibilidade/criar/', views.criar_editar_disponibilidade, name='criar_disponibilidade'),

    # URL para excluir uma disponibilidade
    path('disponibilidade/excluir/<int:disponibilidade_id>/', views.excluir_disponibilidade, name='excluir_disponibilidade'),
]

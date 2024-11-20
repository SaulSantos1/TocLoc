from django.urls import path
from . import views

urlpatterns = [
    # URL para listar todas as reservas
    path('reservas/', views.lista_reservas, name='listar_reservas'),

    # URL para criar ou editar uma reserva
    path('reserva/criar/', views.criar_editar_reserva, name='criar_reserva'),
    path('reserva/editar/<int:reserva_id>/', views.criar_editar_reserva, name='editar_reserva'),

    # URL para excluir uma reserva
    path('reserva/excluir/<int:reserva_id>/', views.excluir_reserva, name='excluir_reserva'),
]

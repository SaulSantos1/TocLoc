from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('cadastro/', views.user_cadastro, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),  # URL para a página inicial do usuário
    path('', views.home_visitante, name='home_visitante'),  # URL para a página inicial do usuário
    path('usuario/<int:user_id>/editar/', views.editar_usuario, name='editar_usuario'),
]

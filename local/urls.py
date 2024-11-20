from django.urls import path
from .views import lista_locais, criar_local,editar_local, excluir_local, visualizar_mapa

urlpatterns = [
    path('', lista_locais, name='lista_locais'),
    path('novo/', criar_local, name='criar_local'),
    path('<int:local_id>/editar/', editar_local, name='editar_local'),
    path('<int:local_id>/excluir/', excluir_local, name='excluir_local'),
    path('mapa/', visualizar_mapa, name='visualizar_mapa'),
]

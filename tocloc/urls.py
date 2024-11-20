from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('reservas/', include('reservas.urls')),
    path('local/', include('local.urls')),
    path('disponibilidade/', include('disponibilidade.urls')),
]

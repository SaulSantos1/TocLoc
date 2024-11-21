from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ['username', 'email', 'tipo_usuario', 'profile_image', 'is_staff']
    
    # Adiciona o campo 'profile_image' na edição de usuários
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('tipo_usuario', 'profile_image')}),
    )
    
    # Adiciona o campo 'profile_image' na criação de usuários
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('tipo_usuario', 'profile_image')}),
    )

admin.site.register(Usuario, CustomUserAdmin)

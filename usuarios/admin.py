from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ['username', 'email', 'tipo_usuario', 'profile_image', 'is_staff']
    
    # Adiciona os campos personalizados na edição de usuários
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('tipo_usuario', 'profile_image')}),
    )
    
    # Adiciona os campos personalizados na criação de usuários
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('tipo_usuario', 'profile_image')}),
    )

    # Redefinição de senha no admin
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return (
            (None, {'fields': ('username', 'password')}),
            ('Informações Pessoais', {'fields': ('email', 'first_name', 'last_name', 'profile_image')}),
            ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
            ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
            ('Tipo de Usuário', {'fields': ('tipo_usuario',)}),
        )

    # Método para adicionar link de redefinição de senha
    change_password_form = UserAdmin.change_password_form
    change_password_template = None  # Use o template padrão do Django para isso

admin.site.register(Usuario, CustomUserAdmin)

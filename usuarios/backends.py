from .models import Usuario
from django.core.exceptions import MultipleObjectsReturned

class EmailOrUsernameBackend:
    def authenticate(username=None, password=None):
        try:
            # Tenta buscar o usuário por username
            user = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            try:
                # Caso não encontre por username, tenta buscar pelo email
                user = Usuario.objects.get(email=username)
            except Usuario.DoesNotExist:
                return None
            except MultipleObjectsReturned:
                # Caso haja múltiplos usuários com o mesmo email
                return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None

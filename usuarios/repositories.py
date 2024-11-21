from .models import Usuario

class UsuarioRepository:
    @staticmethod
    def get_usuario_by_id(user_id):
        """Obtém um usuário pelo ID."""
        return Usuario.objects.filter(id=user_id).first()

    @staticmethod
    def update_usuario(usuario, data):
        """Atualiza as informações de um usuário."""
        for key, value in data.items():
            setattr(usuario, key, value)
        usuario.save()
        return usuario

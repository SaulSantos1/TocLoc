from .repositories import UsuarioRepository

class UsuarioService:
    @staticmethod
    def get_usuario(user_id):
        """Busca o usuário pelo ID."""
        usuario = UsuarioRepository.get_usuario_by_id(user_id)
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        return usuario

    @staticmethod
    def update_usuario(user_id, data):
        """Atualiza os dados do usuário."""
        usuario = UsuarioService.get_usuario(user_id)
        return UsuarioRepository.update_usuario(usuario, data)

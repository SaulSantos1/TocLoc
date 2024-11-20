# services/local_service.py
from .repositories import LocalRepository
from .models import LocalEsportivo

class LocalService:
    @staticmethod
    def listar_locais(usuario):
        if usuario.is_anfitriao():
            return LocalRepository.get_locais_by_anfitriao(usuario)
        elif usuario.is_usuario() or usuario.is_visitante():
            return LocalRepository.get_all_locais()
        return []

    @staticmethod
    def criar_local(data, anfitriao):
        data['anfitriao'] = anfitriao
        local = LocalEsportivo(**data)
        LocalRepository.save_local(local)
        return local

    @staticmethod
    def editar_local(data, local_id):
        local = LocalRepository.get_local_by_id(local_id)
        if local:
            for key, value in data.items():
                setattr(local, key, value)
            LocalRepository.save_local(local)
        return local

    @staticmethod
    def excluir_local(local_id):
        local = LocalRepository.get_local_by_id(local_id)
        if local:
            LocalRepository.delete_local(local)

    @staticmethod
    def listar_anfitriaos():
        # Recupera todos os anfitriões associados a locais
        return LocalRepository.get_all_anfitriaos()
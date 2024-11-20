# repositories/local_repository.py
from .models import LocalEsportivo
from usuarios.models import Usuario

class LocalRepository:
    @staticmethod
    def get_all_locais():
        return LocalEsportivo.objects.all()

    @staticmethod
    def get_locais_by_anfitriao(anfitriao):
        return LocalEsportivo.objects.filter(anfitriao=anfitriao)

    @staticmethod
    def get_local_by_id(local_id):
        return LocalEsportivo.objects.filter(id=local_id).first()

    @staticmethod
    def delete_local(local):
        local.delete()

    @staticmethod
    def save_local(local):
        local.save()

    @staticmethod
    def get_all_anfitriaos():
        # Pega todos os anfitriões únicos associados a locais
        anfitriaos_ids = LocalEsportivo.objects.values('anfitriao').distinct()
        
        # Recupera os usuários (anfitriões) com os IDs encontrados
        return Usuario.objects.filter(id__in=[anfitriao['anfitriao'] for anfitriao in anfitriaos_ids])

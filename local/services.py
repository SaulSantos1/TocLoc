# services/local_service.py
from .repositories import LocalRepository
from .models import LocalEsportivo
from django.shortcuts import get_object_or_404
from usuarios.models import Usuario

class LocalService:
    @staticmethod
    def listar_locais(usuario=None):
        if usuario == None:
            return LocalRepository.get_all_locais()
        else:
            if usuario.is_anfitriao():
                return LocalRepository.get_locais_by_anfitriao(usuario)
            else:
                return LocalRepository.get_all_locais()

    @staticmethod
    def criar_local(data, anfitriao):
        data['anfitriao'] = anfitriao
        local = LocalEsportivo(**data)
        LocalRepository.save_local(local)
        return local

    @staticmethod
    def editar_local(data, local_id):
        # Obtém o local ou retorna 404 se não encontrado
        local = get_object_or_404(LocalEsportivo, id=local_id)

        # Atualiza os atributos do local com os dados fornecidos
        local.nome = data.get('nome', local.nome)
        local.endereco = data.get('endereco', local.endereco)
        local.capacidade = data.get('capacidade', local.capacidade)

        anfitriao_username = data.get('anfitriao')
        if anfitriao_username:
            anfitriao = get_object_or_404(Usuario, username=anfitriao_username)
            local.anfitriao = anfitriao

        # Salva as alterações no banco de dados
        local.save()

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
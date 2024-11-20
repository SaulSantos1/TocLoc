from .models import Disponibilidade

class DisponibilidadeRepository:
    @staticmethod
    def listar_disponibilidades():
        return Disponibilidade.objects.all()

    @staticmethod
    def buscar_disponibilidade_por_id(disponibilidade_id):
        return Disponibilidade.objects.filter(id=disponibilidade_id).first()

    @staticmethod
    def salvar_disponibilidade(disponibilidade):
        disponibilidade.save()

    @staticmethod
    def excluir_disponibilidade(disponibilidade):
        disponibilidade.delete()

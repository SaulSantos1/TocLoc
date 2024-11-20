from .repositories import DisponibilidadeRepository
from .models import Disponibilidade

class DisponibilidadeService:
    @staticmethod
    def listar_disponibilidades():
        return DisponibilidadeRepository.listar_disponibilidades()

    @staticmethod
    def buscar_disponibilidade_por_id(disponibilidade_id):
        return DisponibilidadeRepository.buscar_disponibilidade_por_id(disponibilidade_id)

    @staticmethod
    def criar_ou_atualizar_disponibilidade(data, disponibilidade=None):
        if disponibilidade is None:
            disponibilidade = Disponibilidade()
        
        # Preenche os dados do modelo
        disponibilidade.local = data.get('local')
        disponibilidade.data = data.get('data')
        disponibilidade.horario_inicio = data.get('horario_inicio')
        disponibilidade.horario_fim = data.get('horario_fim')
        
        # Salva a disponibilidade
        DisponibilidadeRepository.salvar_disponibilidade(disponibilidade)
        return disponibilidade

    @staticmethod
    def excluir_disponibilidade(disponibilidade_id):
        disponibilidade = DisponibilidadeRepository.buscar_disponibilidade_por_id(disponibilidade_id)
        if disponibilidade:
            DisponibilidadeRepository.excluir_disponibilidade(disponibilidade)
            return True
        return False

from .repositories import ReservaRepository
from .models import Reserva

class ReservaService:

    @staticmethod
    def listar_reservas():
        return ReservaRepository.listar_reservas()

    @staticmethod
    def obter_reserva(reserva_id):
        return ReservaRepository.obter_reserva(reserva_id)

    @staticmethod
    def criar_reserva(local, usuario, data_reserva, data_checkin=None, data_cancelamento=None):
        # Adicionar lógica de validação de negócios, se necessário
        reserva = ReservaRepository.criar_reserva(local, usuario, data_reserva, data_checkin, data_cancelamento)
        return reserva

    @staticmethod
    def atualizar_reserva(reserva_id, local=None, usuario=None, data_reserva=None, 
                           data_checkin=None, data_cancelamento=None):
        # Adicionar lógica de validação de negócios, se necessário
        reserva = ReservaRepository.atualizar_reserva(reserva_id, local, usuario, data_reserva, 
                                                      data_checkin, data_cancelamento)
        return reserva

    @staticmethod
    def excluir_reserva(reserva_id):
        reserva = ReservaRepository.excluir_reserva(reserva_id)
        return reserva

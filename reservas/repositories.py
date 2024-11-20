from .models import Reserva

class ReservaRepository:

    @staticmethod
    def listar_reservas():
        """Retorna todas as reservas"""
        return Reserva.objects.all()

    @staticmethod
    def obter_reserva(reserva_id):
        """Retorna uma reserva específica pelo ID"""
        return Reserva.objects.get(id=reserva_id)

    @staticmethod
    def criar_reserva(local, usuario, data_reserva, data_checkin=None, data_cancelamento=None):
        """Cria uma nova reserva"""
        reserva = Reserva(local=local, usuario=usuario, data_reserva=data_reserva, 
                          data_checkin=data_checkin, data_cancelamento=data_cancelamento)
        reserva.save()
        return reserva

    @staticmethod
    def atualizar_reserva(reserva_id, local=None, usuario=None, data_reserva=None, 
                           data_checkin=None, data_cancelamento=None):
        """Atualiza uma reserva existente"""
        reserva = Reserva.objects.get(id=reserva_id)
        if local:
            reserva.local = local
        if usuario:
            reserva.usuario = usuario
        if data_reserva:
            reserva.data_reserva = data_reserva
        if data_checkin:
            reserva.data_checkin = data_checkin
        if data_cancelamento:
            reserva.data_cancelamento = data_cancelamento
        reserva.save()
        return reserva

    @staticmethod
    def excluir_reserva(reserva_id):
        """Exclui uma reserva"""
        reserva = Reserva.objects.get(id=reserva_id)
        reserva.delete()
        return reserva

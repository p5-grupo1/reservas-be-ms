from reservas_app.models.reserva    import Reserva
from rest_framework                 import serializers

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Reserva
        fields = ['idReserva', 'cuentaJardinero', 'idPublicacion', 'cuentaCliente']

    def to_representation(self, obj):
        reservas = Reserva.objects.get(idReserva=obj.idReserva)
        return {
            'idReserva' :   reservas.idReserva,
            'cuentaJardinero'   : reservas.cuentaJardinero,
            'idPublicacion'     : reservas.idPublicacion,
            'cuentaCliente'     : reservas.cuentaCliente,
            'fechaReserva'      : reservas.fechaReserva
        }
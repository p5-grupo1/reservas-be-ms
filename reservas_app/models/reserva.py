from django.db                  import models

class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    cuentaJardinero = models.CharField(max_length=60, null=False)
    idPublicacion = models.CharField(max_length=120, null=False)
    cuentaCliente = models.CharField(max_length=60, null= False)
    fechaReserva  = models.DateTimeField(auto_now_add=True)





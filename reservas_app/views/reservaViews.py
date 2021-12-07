from django.db.models import query
from rest_framework                 import generics, serializers, status
from rest_framework.response        import Response
from reservas_app.models.reserva    import Reserva
from reservas_app.serializers.reservaSerializer import ReservaSerializer
from django_filters.rest_framework              import DjangoFilterBackend

class CreateReserva(generics.CreateAPIView):
    serializer_class = ReservaSerializer

    def post(self, request, *args, **kwargs):
        serializer = ReservaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Reserva Creada", status=status.HTTP_201_CREATED)

    
class DeleteReserva(generics.DestroyAPIView):
    serializers_class = ReservaSerializer
    queryset = Reserva.objects.all()

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



class ListaReservas(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cuentaCliente', 'cuentaJardinero']
    serializer_class = ReservaSerializer

    def get_queryset(self):
        queryset = Reserva.objects.all()
        return queryset



class ByClientesReservas(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cuentaCliente']
    serializer_class = ReservaSerializer

    def get_queryset(self):
        queryset = Reserva.objects.all()
        return queryset

class DetailReservas(generics.RetrieveAPIView):
    serializer_class = ReservaSerializer
    queryset = Reserva.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class AllReservas(generics.ListAPIView):
    serializer_class = ReservaSerializer

    def get_queryset(self):
        queryset = Reserva.objects.all()
        return queryset





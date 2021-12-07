from django.contrib import admin
from django.urls import path, re_path
from reservas_app import views as Views 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions




schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de API",
      default_version='v0.1',
      description="Documentacion publica de API de reservas",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="cdospinav16@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('createreserva/', Views.CreateReserva.as_view()), #Creacion de reserva
    path('deletereserva/<int:pk>', Views.DeleteReserva.as_view()), #Eliminacion de reserva
    path('allreservas/', Views.AllReservas.as_view()),  #Listado de todas las reservas
    path('reserva/<int:pk>', Views.DetailReservas.as_view()), #Listar por ID de la reserva
    path('reservasfilter/cliente', Views.ByClientesReservas.as_view()), # Lista todas las reservas de un cliente
    path('reservasfilter/clientejardinero/', Views.ListaReservas.as_view()), #Filtra reservas por username cliente y jardi


    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

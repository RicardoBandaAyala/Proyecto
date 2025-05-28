from rest_framework import generics
from .models import Espacio, Reserva, Cliente
from .serializers import EspacioSerializer, ReservaSerializer, ClienteSerializer
# API para la aplicación de reservas

# Esta API proporciona endpoints para gestionar reservas, espacios y clientes
class EspacioList(generics.ListAPIView):
    queryset = Espacio.objects.filter(disponible=True)
    serializer_class = EspacioSerializer

# Esta vista lista todos los espacios disponibles para reservar
class ReservaList(generics.ListAPIView):
    serializer_class = ReservaSerializer

    def get_queryset(self):
        cliente = self.request.query_params.get('cliente')
        if cliente:
            return Reserva.objects.filter(cliente__nombre__icontains=cliente)
        return Reserva.objects.all()

# Esta vista lista todas las reservas, filtrando por cliente si se proporciona un parámetro
class CrearReserva(generics.CreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

# Esta vista permite crear una nueva reserva para un espacio específico
class ClienteDetail(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Esta vista permite obtener los detalles de un cliente específico
class ActualizarEstadoReserva(generics.UpdateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

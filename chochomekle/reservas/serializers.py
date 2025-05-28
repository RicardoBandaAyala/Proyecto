from rest_framework import serializers
from .models import Espacio, Reserva, Cliente
# Estos serializers convierten los modelos a formatos JSON para la API REST

# Serializador para el modelo Espacio
class EspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacio
        fields = '__all__'

# Serializador para el modelo Reserva
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

# Serializador para el modelo Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

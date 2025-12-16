from rest_framework import serializers
from .models import Cliente, Taller, Vehiculo, Mantencion

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    # Aquí un truco: Queremos ver el nombre del cliente, no solo su número ID
    nombre_cliente = serializers.ReadOnlyField(source='cliente.nombre')

    class Meta:
        model = Vehiculo
        fields = '__all__'

class MantencionSerializer(serializers.ModelSerializer):
    # Para que en la API se vea la patente y no solo el ID del auto
    patente_vehiculo = serializers.ReadOnlyField(source='vehiculo.patente')
    nombre_cliente = serializers.ReadOnlyField(source='cliente.nombre')

    class Meta:
        model = Mantencion
        fields = '__all__'
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Cliente, Taller, Vehiculo, Mantencion
from .serializers import (
    ClienteSerializer, TallerSerializer, VehiculoSerializer, MantencionSerializer
)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['rut', 'nombre'] # Buscador por RUT o Nombre
    permission_classes = [permissions.IsAuthenticated]
    

class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer
    permission_classes = [permissions.IsAuthenticated]

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['patente', 'vin']
    filterset_fields = ['marca', 'cliente'] # Filtros rápidos
    permission_classes = [permissions.IsAuthenticated]

class MantencionViewSet(viewsets.ModelViewSet):
    queryset = Mantencion.objects.all().order_by('-fecha_ingreso')
    serializer_class = MantencionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # --- Filtros ---
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    # Filtros pedidos: Tipo mantención, fecha y kilometraje
    filterset_fields = {
        'tipo_servicio': ['exact'],
        'fecha_ingreso': ['gte', 'lte'], # Filtrar por rango de fechas (desde/hasta)
        'kilometraje': ['gte', 'lte'],   # Filtrar por kilometraje (mayor/menor que)
        'estado': ['exact'],
        'taller': ['exact'],
    }
    
    # Buscador general
    search_fields = ['cliente__nombre', 'vehiculo__patente', 'descripcion_falla']
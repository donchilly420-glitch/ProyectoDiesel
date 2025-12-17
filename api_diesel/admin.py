from django.contrib import admin
from .models import Cliente, Taller, Vehiculo, Mantencion

# Configuración para el CLIENTE
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'telefono', 'es_empresa')
    search_fields = ('rut', 'nombre')

# Configuración para el VEHICULO
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca', 'modelo', 'anio', 'cliente')
    search_fields = ('patente', 'vin', 'cliente__nombre')
    list_filter = ('marca',)

# Configuración para la MANTENCION 
@admin.register(Mantencion)
class MantencionAdmin(admin.ModelAdmin):
    # Qué columnas se ven en la lista
    list_display = ('id', 'get_identificador', 'tipo_servicio', 'estado', 'fecha_ingreso', 'costo_total')
    # Filtros laterales (muy útil para ver "Solo pendientes" o "Solo inyectores")
    list_filter = ('estado', 'tipo_servicio', 'taller')
    # Buscador (busca por nombre del cliente, patente del auto o ID de la orden)
    search_fields = ('cliente__nombre', 'vehiculo__patente', 'id')
    # Ordenar por fecha (el más nuevo primero)
    ordering = ('-fecha_ingreso',)

    # Método personalizado para mostrar Patente o "Pieza Suelta" en la lista
    def get_identificador(self, obj):
        if obj.vehiculo:
            return obj.vehiculo.patente
        return "PIEZA SUELTA"
    get_identificador.short_description = "Vehículo / Item"

# Registro simple para el TALLER
admin.site.register(Taller)

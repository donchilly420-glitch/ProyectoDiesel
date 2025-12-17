from django.db import models

# Create your models here.
# 1. MODELO CLIENTE
# Necesitamos saber de quién es el fierro o el vehículo.
class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True, help_text="RUT con puntos y guión")
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    es_empresa = models.BooleanField(default=False, help_text="¿Es flota o empresa?")

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

# 2. MODELO TALLER 
# Define el área donde se realiza el trabajo.
class Taller(models.Model):
    AREAS_CHOICES = [
        ('LAB', 'Laboratorio Diesel (Banco de Pruebas)'),
        ('MEC', 'Mecánica General (Patio)'),
        ('LAV', 'Zona de Lavado'),
    ]
    nombre = models.CharField(max_length=50)
    tipo_area = models.CharField(max_length=3, choices=AREAS_CHOICES)
    encargado = models.CharField(max_length=100, help_text="Jefe de taller o encargado del área")

    def __str__(self):
        return f"{self.nombre} - {self.get_tipo_area_display()}"

# 3. MODELO VEHICULO
class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vehiculos')
    patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(verbose_name="Año")
    vin = models.CharField(max_length=30, blank=True, null=True, verbose_name="Número de Chasis/VIN")
    tipo_motor = models.CharField(max_length=50, blank=True, help_text="Ej: Common Rail, Convencional, Electrónico")

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"

# 4. MODELO MANTENCION (La Orden de Trabajo)
# Puede ser a un vehículo O a una pieza suelta.
class Mantencion(models.Model):
    # Estados del trabajo
    ESTADOS = [
        ('ING', 'Ingresado / En Espera'),
        ('DIAG', 'En Diagnóstico'),
        ('REP', 'En Reparación / Calibración'),
        ('ESP', 'Esperando Repuestos'),
        ('LISTO', 'Listo para Entrega'),
        ('ENTR', 'Entregado'),
    ]

    # Tipos de Servicio 
    TIPOS_SERVICIO = [
        ('PREV', 'Mantención Preventiva'),
        ('INY', 'Reparación/Calibración Inyectores'),
        ('BOM', 'Reparación/Calibración Bomba'),
        ('MEC', 'Mecánica (Sacar/Poner)'),
        ('LAV', 'Lavado de Estanque'),
        ('COMP', 'Servicio Completo (Mecánica + Laboratorio)'),
    ]

    # Niveles de combustible (Solo si hay vehículo)
    NIVEL_COMBUSTIBLE = [
        ('RES', 'Reserva'),
        ('1/4', 'Un Cuarto'),
        ('1/2', 'Medio Estanque'),
        ('3/4', 'Tres Cuartos'),
        ('FULL', 'Lleno'),
    ]

    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_entrega_estimada = models.DateField(null=True, blank=True)
    
    # Relaciones
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    taller = models.ForeignKey(Taller, on_delete=models.SET_NULL, null=True, help_text="Área responsable")
    
    # El vehículo es OPCIONAL (null=True) para trabajos de solo banco (bomba en mano)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True)

    # Detalles del trabajo
    tipo_servicio = models.CharField(max_length=4, choices=TIPOS_SERVICIO)
    estado = models.CharField(max_length=5, choices=ESTADOS, default='ING')
    descripcion_falla = models.TextField(help_text="Lo que el cliente dice que falla")
    observaciones_tecnicas = models.TextField(blank=True, help_text="Diagnóstico del mecánico/bombero")
    
    # Datos específicos
    kilometraje = models.PositiveIntegerField(null=True, blank=True)
    nivel_combustible = models.CharField(max_length=4, choices=NIVEL_COMBUSTIBLE, null=True, blank=True)
    
    # Costo
    costo_total = models.PositiveIntegerField(default=0, help_text="Valor en pesos chilenos")

    def __str__(self):
        if self.vehiculo:
            return f"OT #{self.id} - {self.vehiculo.patente} - {self.get_tipo_servicio_display()}"
        return f"OT #{self.id} - PIEZA SUELTA ({self.cliente.nombre}) - {self.get_tipo_servicio_display()}"
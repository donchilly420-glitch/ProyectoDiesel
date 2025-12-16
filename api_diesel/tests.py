from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Cliente, Vehiculo

class ClienteModelTest(TestCase):
    def setUp(self):
        # Creamos un cliente de prueba
        self.cliente = Cliente.objects.create(
            rut="11.222.333-4",
            nombre="Cliente De Prueba",
            telefono="912345678"
        )

    def test_creacion_cliente(self):
        """Prueba que el cliente se guarda correctamente"""
        self.assertEqual(self.cliente.nombre, "Cliente De Prueba")
        self.assertEqual(self.cliente.rut, "11.222.333-4")

    def test_str_cliente(self):
        """Prueba que el texto del cliente sea 'Nombre (RUT)'"""
        esperado = "Cliente De Prueba (11.222.333-4)"
        self.assertEqual(str(self.cliente), esperado)
from django.contrib import admin
from django.urls import path, include
# Importamos lo necesario para la documentación Swagger 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Servicio Diesel",
      default_version='v1',
      description="API para gestión de taller de inyección y mecánica",
      contact=openapi.Contact(email="taller@diesel.cl"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_diesel.urls')), # <-- Conectamos tu app aquí
    
    # Rutas de Documentación
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
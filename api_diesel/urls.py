from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, TallerViewSet, VehiculoViewSet, MantencionViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'talleres', TallerViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'mantenciones', MantencionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
]
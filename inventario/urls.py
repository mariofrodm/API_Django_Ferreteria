from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, PiezaViewSet, AsignacionPiezaViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'piezas', PiezaViewSet)
router.register(r'asignaciones', AsignacionPiezaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import viewsets
from .models import Producto, Pieza, AsignacionPieza
from .serializers import ProductoSerializer, PiezaSerializer, AsignacionPiezaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PiezaViewSet(viewsets.ModelViewSet):
    queryset = Pieza.objects.all()
    serializer_class = PiezaSerializer

class AsignacionPiezaViewSet(viewsets.ModelViewSet):
    queryset = AsignacionPieza.objects.all()
    serializer_class = AsignacionPiezaSerializer

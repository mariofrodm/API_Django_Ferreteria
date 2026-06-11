from rest_framework import serializers
from .models import Producto, Pieza, AsignacionPieza

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class PiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pieza
        fields = '__all__'

class AsignacionPiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionPieza
        fields = '__all__'

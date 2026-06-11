from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True, db_column='ProductoId')
    nombre = models.CharField(max_length=100, db_column='Nombre')
    descripcion = models.CharField(max_length=300, blank=True, null=True, db_column='Descripcion')
    precio = models.DecimalField(max_digits=18, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], db_column='Precio')
    fecha_mod = models.DateTimeField(auto_now=True, db_column='FechaMod')
    activo = models.BooleanField(default=True, db_column='Activo')

    class Meta:
        db_table = 'Producto'

    def __str__(self):
        return self.nombre

class Pieza(models.Model):
    pieza_id = models.AutoField(primary_key=True, db_column='PiezaId')
    nombre = models.CharField(max_length=100, db_column='Nombre')
    descripcion = models.CharField(max_length=300, blank=True, null=True, db_column='Descripcion')
    material = models.CharField(max_length=100, db_column='Material')
    es_original = models.BooleanField(default=False, db_column='EsOriginal')
    fecha_mod = models.DateTimeField(auto_now=True, db_column='FechaMod')
    activo = models.BooleanField(default=True, db_column='Activo')

    class Meta:
        db_table = 'Pieza'

    def __str__(self):
        return self.nombre

class AsignacionPieza(models.Model):
    asignacion_pieza_id = models.AutoField(primary_key=True, db_column='AsignacionPiezaId')
    cantidad = models.IntegerField(validators=[MinValueValidator(1)], db_column='Cantidad')
    fecha_mod = models.DateTimeField(auto_now=True, db_column='FechaMod')
    activo = models.BooleanField(default=True, db_column='Activo')
    pieza = models.ForeignKey(Pieza, on_delete=models.RESTRICT, db_column='PiezaId')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='ProductoId')

    class Meta:
        db_table = 'AsignacionPieza'

    def __str__(self):
        return f"{self.cantidad}x {self.pieza.nombre} -> {self.producto.nombre}"

from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion = models.TextField()
    marca = models.CharField(max_length = 50)
    cantidad_min = models.IntegerField()
    cantidad_max = models.IntegerField()
    precio = models.DecimalField(max_digits = 5, decimal_places = 2)
    estado = models.CharField(choices=[("1", "Activo"), ("0", "Inactivo")], default="1", max_length=10)

    def __str__(self) -> str:
        return self.nombre

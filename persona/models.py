from django.contrib.auth.hashers import make_password
from django.db import models

class Persona(models.Model):
    TIPOS_DOCUMENTO = [
        ("CC", "Cédula de Ciudadanía"),
        ("TI", "Tarjeta de Identidad"),
        ("CE", "Cédula de Extranjería"),
        ("PA", "Pasaporte"),
        # Agrega más tipos de documento según tus necesidades
    ]

    tipo_documento = models.CharField(max_length=2, choices=TIPOS_DOCUMENTO)
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(choices=[("M", "Masculino"), ("F", "Femenino"), ("O", "Otro")], max_length=1, blank=True, null=True)
    estado_civil = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(choices=[("1", "Activo"), ("0", "Inactivo")], default="1", max_length=10)
    password = models.CharField(max_length=128, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Si la contraseña aún no se ha establecido, establecerla como el documento
        if not self.password:
            self.password = make_password(self.documento)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"




from django.db import models

# Create your models here.

class Cliente (models.Model):
    nombre=models.TextField(max_length=255)
    usuario=models.TextField(max_length=255)
    correo=models.CharField(max_length=255)
    edad=models.PositiveIntegerField()
    def __str__(self):
        return f'Usuario:{self.usuario}'



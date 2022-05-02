from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    correo_electronico=models.EmailField(max_length=30)
    telefono=models.CharField(max_length=15)
    direccion=models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Proveedor(models.Model):

    nombre=models.CharField(max_length=50) 

    razon_social=models.CharField(max_length=50) 

    telefono=models.CharField(max_length=50) 

    correo_electronico=models.EmailField(max_length=50) 

    categoria=models.CharField(max_length=50)

    def __str__(self): 
        return '%s %s' % (self.nombre, self.razon_social) 
from django.db import models
import datetime

# Create your models here.
class Factura(models.Model):
    n_factura = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    neto = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()
    fecha_emision= models.DateField(datetime.date.today())

    def __str__(self):
        return self.n_factura


class Proveedor(models.Model):
    rut = models.CharField(max_length=100)
    razon = models.CharField(max_length=100)
    giro = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="Mail del profesor", unique=True)
    telefono = models.CharField(max_length=15, default="")
    tipo_venta = models.CharField(max_length=15, default="")
    
    def __str__(self):
        return self.rut


class Consumidor(models.Model):
    nombre= models.CharField(max_length=100)
    rut= models.CharField(max_length=100)
    giro= models.CharField(max_length=100)
    direccion= models.CharField(max_length=100)
    comuna= models.CharField(max_length=100)
    ciudad= models.CharField(max_length=100)
    tipo_compra= models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


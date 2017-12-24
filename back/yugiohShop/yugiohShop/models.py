from django.db import models
from django.utils import timezone

class Producto(models.Model):
    # id = models.AutoField(primary_key = true)
    tipoProducto = models.CharField(max_length = 2) #C (carta) o O (otros)
    nombre = models.CharField(max_length = 100)
    precio = models.FloatField()
    stock = models.IntegerField()
    fechaIngreso = models.DateTimeField()


class Carta(models.Model):
    # id = models.AutoField(primary_key = true)
    passCode = models.IntegerField()
    nombreEspanol = models.CharField(max_length = 250)
    nombreIngles = models.CharField(max_length = 250)
    tipoCarta = models.CharField(max_length = 2) # M (Monster) S (Spell) T (Trap)
    atributo = models.CharField(max_length = 20)
    tipo = models.CharField(max_length = 50)
    tipoMonstruo = models.CharField(max_length = 50)
    nivel = models.IntegerField()
    ataque = models.IntegerField() #-1 cuando es S o T
    defensa = models.IntegerField() #-1 cuando es S o T
    descripcion = models.TextField()
    imagen = models.CharField(max_length = 250)
    arquetipo = models.ForeignKey ('Arquetipo', on_delete=models.CASCADE)
    idProducto = models.ForeignKey ('Producto', on_delete=models.CASCADE)

class Arquetipo(models.Model):
    # id = model.AutoField(primary_key = true)
    nombre  = models.CharField(max_length = 250)
    torneosGanadosLocal = models.IntegerField()
    torneosGanadosInternacional = models.IntegerField()

class Origen(models.Model):
    # id = models.AutoField(primary_key = true)
    nombre = models.TextField()
    fechaLanzamiento = models.DateTimeField()
    codigo = models.IntegerField()

class Otros(models.Model):
    # id = models.AutoField(primary_key = true)
    nombre = models.CharField(max_length = 250)
    idProducto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    descripcion = models.TextField()

class CartaXOrigen(models.Model):
    idCarta = models.ForeignKey('Carta', on_delete=models.CASCADE)
    idOrigen = models.ForeignKey('Origen', on_delete=models.CASCADE)
    rareza = models.CharField(max_length = 50)

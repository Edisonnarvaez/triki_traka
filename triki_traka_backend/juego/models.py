#models
from django.db import models

class Partida(models.Model):
    fecha_inicio = models.DateTimeField(auto_now_add=True)

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)

class Movimiento(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    coordenada_fila = models.IntegerField()
    coordenada_columna = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


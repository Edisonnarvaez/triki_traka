from django.db import models


class Partida(models.Model):
    """Modelo para representar una partida."""
    fecha_inicio = models.DateTimeField(auto_now_add=True)


class Jugador(models.Model):
    """Modelo para representar un jugador."""
    nombre = models.CharField(max_length=100)


class Movimiento(models.Model):
    """Modelo para representar un movimiento en una partida."""
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    coordenada_fila = models.IntegerField()
    coordenada_columna = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

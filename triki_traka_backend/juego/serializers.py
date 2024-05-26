from rest_framework import serializers
from .models import Partida, Jugador, Movimiento

class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = '__all__'

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = '__all__'

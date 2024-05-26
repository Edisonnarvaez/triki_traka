# juego/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('partidas/', views.obtener_partidas, name='obtener_partidas'),
    path('partidas/crear/', views.crear_partida, name='crear_partida'),
    path('partidas/<int:partida_id>/', views.gestionar_partida, name='gestionar_partida'),
]

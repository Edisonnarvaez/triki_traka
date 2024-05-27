"""
URL configuration for triki_traka_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# triki_traka_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('juego.urls')),  # Incluye las URLs de la aplicación 'juego'
    path('', include('juego.urls')),  # Redirige la URL principal a las URLs de 'juego'
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('partidas/', views.obtener_partidas, name='obtener_partidas'),
#     path('partidas/crear/', views.crear_partida, name='crear_partida'),
#     path('partidas/<int:partida_id>/', views.gestionar_partida, name='gestionar_partida'),
# ]

# Generated by Django 5.0.6 on 2024-05-26 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordenada_fila', models.IntegerField()),
                ('coordenada_columna', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juego.jugador')),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juego.partida')),
            ],
        ),
    ]
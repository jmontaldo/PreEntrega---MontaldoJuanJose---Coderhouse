# Generated by Django 5.0.4 on 2024-05-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vuelos', '0003_destinos_alter_vuelos_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vuelos',
            name='fecha',
            field=models.DateField(null=True, verbose_name='Fecha de salida'),
        ),
    ]

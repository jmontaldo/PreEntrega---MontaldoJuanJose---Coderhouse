# Generated by Django 5.0.4 on 2024-05-11 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0002_alter_vuelos_numero_documento'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vuelos',
            new_name='Clientes',
        ),
    ]

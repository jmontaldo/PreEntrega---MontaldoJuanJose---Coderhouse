# Generated by Django 5.0.4 on 2024-05-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vuelos', '0002_alter_vuelos_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(verbose_name='Descripción')),
            ],
        ),
        migrations.AlterField(
            model_name='vuelos',
            name='codigo',
            field=models.IntegerField(unique=True, verbose_name='Código'),
        ),
    ]

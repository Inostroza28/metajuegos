# Generated by Django 4.2 on 2023-04-18 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_credencial_delete_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='Codigo_producto')),
                ('nombre_producto', models.CharField(max_length=30, verbose_name='Nombre_producto')),
                ('categoria', models.CharField(max_length=20, verbose_name='Categoria_producto')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_carrito', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id_carrito')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]

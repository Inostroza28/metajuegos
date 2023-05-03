# Generated by Django 4.2 on 2023-05-02 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_delete_cuenta_alter_mascota_raza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoJuego', models.IntegerField(verbose_name='Id Juego')),
                ('nombreJuego', models.CharField(max_length=60, verbose_name='Nombre Juego')),
                ('genero', models.IntegerField(verbose_name='Genero Juego')),
                ('plataforma', models.IntegerField(verbose_name='Plataforma')),
            ],
        ),
        migrations.DeleteModel(
            name='Mascota',
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-26 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0074_auto_20200325_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='correoCliente',
            new_name='Correo_Cliente',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='direccionCliente',
            new_name='Direccion_Cliente',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='idCliente',
            new_name='Id_Cliente',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nombreCliente',
            new_name='Nombre_Cliente',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='telefonoCliente',
            new_name='Telefono_Cliente',
        ),
    ]

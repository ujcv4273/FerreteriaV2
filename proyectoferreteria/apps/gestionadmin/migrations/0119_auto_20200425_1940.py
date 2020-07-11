# Generated by Django 2.2.6 on 2020-04-25 19:40

from django.db import migrations, models
import django.db.models.deletion
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0118_auto_20200424_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Correo_Cliente',
            field=models.EmailField(blank=True, max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarcorreoexistenteCliente], verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Direccion_Empleado',
            field=models.TextField(max_length=100, validators=[proyectoferreteria.apps.gestionadmin.models.validardireccion], verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Telefono_Empleado',
            field=models.CharField(max_length=8, validators=[proyectoferreteria.apps.gestionadmin.models.validarnumero], verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Codigo_CAI',
            field=models.CharField(default='114-560-345KJ', max_length=35, verbose_name='Código CAI'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Id_MetodoPago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.MetodoPago', verbose_name='Método de pago'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Numero_Sar',
            field=models.CharField(default='004-340-345KN', max_length=15, verbose_name='Número de la SAR'),
        ),
        migrations.AlterField(
            model_name='garantia',
            name='Tiempo_Garantia_Mes',
            field=models.IntegerField(verbose_name='Tiempo garantía'),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='descripcionMetodoPago',
            field=models.TextField(max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre], verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Existencia_Minima',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validar_mayor_a_tres], verbose_name='Existencia Mínima'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Id_Categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Categoria', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Id_Garantia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Garantia', verbose_name='Garantía'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='Correo_Proveedor',
            field=models.EmailField(blank=True, max_length=30, null=True, validators=[proyectoferreteria.apps.gestionadmin.models.validarcorreoexistenteProveedor], verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='Telefono_Proveedor',
            field=models.CharField(max_length=8, validators=[proyectoferreteria.apps.gestionadmin.models.validarnumero], verbose_name='Teléfono'),
        ),
    ]
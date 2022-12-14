# Generated by Django 4.0.6 on 2022-08-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CLIENTES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('razonSocial', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('codigoPostal', models.IntegerField()),
                ('telefono', models.CharField(max_length=50)),
                ('eMail', models.EmailField(max_length=50)),
                ('form_pago', models.CharField(max_length=50)),
                ('codigo_Cliente', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DIRECTORIO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('codigoPostal', models.IntegerField()),
                ('cargo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EMPLEADO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('codigoPostal', models.IntegerField()),
                ('telefono', models.CharField(max_length=50)),
                ('eMail', models.EmailField(max_length=50)),
                ('puesto', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('horarioIngreso', models.TimeField()),
                ('horarioSalida', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PRODUCTO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monodroga', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('presentacion', models.CharField(max_length=50)),
                ('formFarmaceutica', models.CharField(max_length=50)),
                ('certificado', models.IntegerField()),
                ('codigoProducto', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PROVEEDORES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('razonSocial', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('codigoPostal', models.IntegerField()),
                ('telefono', models.CharField(max_length=50)),
                ('eMail', models.EmailField(max_length=50)),
                ('form_pago', models.CharField(max_length=50)),
                ('codigo_Proveedor', models.CharField(max_length=50)),
                ('tipo_Cliente', models.CharField(max_length=50)),
            ],
        ),
    ]

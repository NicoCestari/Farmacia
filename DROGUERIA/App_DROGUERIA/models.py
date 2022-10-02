from dataclasses import field
import imaplib
import mimetypes
from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User

# Create your models here.
class DIRECTORIO(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    cargo = models.CharField(max_length=50)
    # Usuario = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'Apellido y nombre: {self.apellido}, {self.nombre} || Edad: {self.edad} || Cargo  {self.cargo}'
class EMPLEADO(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    telefono = models.CharField(max_length=50)
    eMail = models.EmailField(max_length=50)
    puesto = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    horarioIngreso = models.TimeField()
    horarioSalida = models.TimeField()
    # Usuario = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'Nombre y Apellido: {self.nombre} {self.apellido} - Direccion: {self.direccion} - C.P.: {self.codigoPostal} - Telefono: {self.telefono} - E-mail: {self.eMail} - Puesto {self.puesto} - Cargo {self.cargo} - Horario Ingreso: {self.horarioIngreso} // Horario Salida: {self.horarioSalida} '
class PRODUCTO(models.Model):
    monodroga = models.CharField(max_length=50)
    marca = models.CharField(max_length=50) # Del laboratorio productor - Ej. Rivero, Drawer, Klonal, Bayer, Bago, etc.
    presentacion = models.CharField(max_length=50) # Presentacion de la caja/BLISTER - Ej.: BLISTER x 15 Comp / CAJA x 100 Ampollas  
    formFarmaceutica = models.CharField(max_length=50) # Comprimido, Capsula, Sachet, Ampolla, Frasco Ampolla, etc.
    certificado = models.IntegerField() # ANMAT
    codigoProducto = models.CharField(max_length=50)
    stock = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.monodroga} | {self.marca} | {self.presentacion} | {self.formFarmaceutica} | {self.certificado} | {self.codigoProducto} | {self.stock}'

    class meta():
        ordering = ('-monodroga',)
class PROVEEDORES(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    razonSocial = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    telefono = models.CharField(max_length=50)
    eMail = models.EmailField(max_length=50)
    form_pago = models.CharField(max_length=50)
    codigo_Proveedor = models.CharField(max_length=50)
    tipo_Proveedor = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'Nombre y Apellido: {self.nombre} {self.apellido} - Razon Social: {self.razonSocial} - Direccion: {self.direccion} - C.P.: {self.codigoPostal} - Teléfono: {self.telefono} - E-mail: {self.eMail} - Forma de Pago: {self.form_pago} - Código Proveedor {self.codigo_Proveedor} - Tipo Cliente: {self.tipo_Proveedor}'
class CLIENTES(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    razonSocial = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    telefono = models.CharField(max_length=50)
    eMail = models.EmailField(max_length=50)
    form_pago = models.CharField(max_length=50)
    codigo_Cliente = models.CharField(max_length=50)
    tipo_Cliente= models.CharField(max_length=50) # Clinica, Hospitales, Ministerios, Municipio, Gobierno Provincial, etc

    def __str__(self) -> str:
        return f'Nombre y Apellido: {self.nombre} {self.apellido} - Razon Social: {self.razonSocial} - Direccion: {self.direccion} - C.P.: {self.codigoPostal} - Teléfono: {self.telefono} - E-mail: {self.eMail} - Forma de Pago: {self.form_pago} - Código Proveedor: {self.codigo_Cliente} - Tipo Cliente: {self.tipo_Cliente}'

class IMAGENES(models.Model):
    imagen = models.ImageField(upload_to="imagenes")
    def __str__(self) -> str:
        return f'Imágen: {self.imagen}'

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='Avatares', blank=True, null=True)
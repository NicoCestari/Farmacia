from django import forms


class CreaProveedor(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    razonSocial = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    codigoPostal = forms.IntegerField()
    telefono = forms.CharField(max_length=50)
    eMail = forms.EmailField(max_length=50)
    form_pago = forms.CharField(max_length=50)
    codigo_Proveedor = forms.CharField(max_length=50)
    tipo_Proveedor= forms.CharField(max_length=50) 


class CreaProducto(forms.Form):
    monodroga = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50) 
    presentacion = forms.CharField(max_length=50) 
    formFarmaceutica = forms.CharField(max_length=50)
    certificado = forms.IntegerField() 
    codigoProducto = forms.CharField(max_length=50)
    stock = forms.IntegerField()

class CreaEmpleado(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    codigoPostal = forms.IntegerField()
    telefono = forms.CharField(max_length=50)
    eMail = forms.EmailField(max_length=50)
    puesto = forms.CharField(max_length=50)
    cargo = forms.CharField(max_length=50)
    horarioIngreso = forms.TimeField()
    horarioSalida = forms.TimeField()

class CreaCliente(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    razonSocial = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    codigoPostal = forms.IntegerField()
    telefono = forms.CharField(max_length=50)
    eMail = forms.EmailField(max_length=50)
    form_pago = forms.CharField(max_length=50)
    codigo_Cliente = forms.CharField(max_length=50)
    tipo_Cliente= forms.CharField(max_length=50)

import imp
from django.shortcuts import redirect, render
from django.http import HttpResponse
from App_DROGUERIA.models import DIRECTORIO, EMPLEADO, PRODUCTO,PROVEEDORES,CLIENTES, Avatar
from .forms import CreaCliente, CreaEmpleado, CreaProducto, CreaProveedor

from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView



# //////// Visualizacion de Templates ////////
def ORIGEN (request):
    try:
        avatar = Avatar.objects.get(usuario = request.user.id)
        return render(request, "00 - ORIGEN.html", {"url": avatar.imagen.url})
    except:
        return render(request, "00 - ORIGEN.html")
def ORIGEN_B (request):
    try:
        avatar = Avatar.objects.get(usuario = request.user.id)
        return render(request, "00 - ORIGEN (b).html", {"url": avatar.imagen.url})
    except:
        return render(request, "00 - ORIGEN (b).html")
def Inicio(request):
    try:
        avatar = Avatar.objects.get(usuario = request.user.id)
        return render(request,"01 - Inicio.html", {"url": avatar.imagen.url})
    except:
        return render(request,"01 - Inicio.html")
def Productos(request):
    productos = PRODUCTO.objects.all()
    try:
        avatar = Avatar.objects.get(usuario = request.user.id)
        return render(request,"02 - Productos.html", {"Vademecum": productos, "url": avatar.imagen.url})
    except:
        return render(request,"02 - Productos.html")
def AcercadeCoderPharma (request):
    try:
        avatar = Avatar.objects.get(usuario = request.user.id)
        return render(request,"04 - AcercadeCoderPharma.html", {"url": avatar.imagen.url})
    except:
        return render(request,"04 - AcercadeCoderPharma.html")
def Directorio (request):
    try:
        avatar = Avatar.objects.get(usuario = request.user.id)
        return render(request,"05 - Directorio.html", {"url": avatar.imagen.url})
    except:
        return render(request,"05 - Directorio.html")
def Empleados (request):
    empleados = EMPLEADO.objects.all()
    try:
        avatar = Avatar.objects.get(usuario = request.user.id)
        return render(request,"06 - Empleados.html", {"Personal": empleados, "url": avatar.imagen.url})
    except:
        return render(request,"06 - Empleados.html", {"Personal": empleados})
def Proveedores (request):
    proveedor = PROVEEDORES.objects.all()
    try:
        avatar = Avatar.objects.get(usuario = request.user.id)
        return render(request,"07 - Proveedores.html", {"Proveedores": proveedor, "url": avatar.imagen.url})
    except:
        return render(request,"07 - Proveedores.html", {"Proveedores": proveedor})
def Clientes (request):
    clientes = CLIENTES.objects.all()
    try:
        avatar = Avatar.objects.get(usuario = request.user.id)
        return render(request,"08 - Clientes.html", {"Clientes": clientes, "url": avatar.imagen.url})
    except:
        return render(request,"08 - Clientes.html", {"Clientes": clientes}) 


# //////// Funciones ////////
# Agrega Cliente
@login_required
def AgregaCliente(request):
    if request.method == 'POST':
        
        formulario = CreaCliente(request.POST)

        if formulario.is_valid():

            dato_cliente = formulario.cleaned_data

            cliente = CLIENTES(
                                    nombre = dato_cliente["nombre"],
                                    apellido = dato_cliente["apellido"],
                                    razonSocial = dato_cliente["razonSocial"],
                                    direccion = dato_cliente["direccion"],
                                    codigoPostal = dato_cliente["codigoPostal"], 
                                    telefono = dato_cliente["telefono"],
                                    eMail = dato_cliente["eMail"],
                                    form_pago = dato_cliente["form_pago"],
                                    codigo_Cliente = dato_cliente["codigo_Cliente"],
                                    tipo_Cliente = dato_cliente["tipo_Cliente"]
                                    )

            cliente.save()

            return redirect("08_Clientes")
        
        return render(request, "08 - AgregaCliente.html", {"form":formulario})
    
    formulario = CreaCliente()

    try:
            avatar = Avatar.objects.get(usuario = request.user.id)
            return render(request, "08 - AgregaCliente.html", {"form":formulario, "url": avatar.imagen.url})
    except:
        return render(request, "08 - AgregaCliente.html", {"form":formulario})
# Edita Cliente
@login_required
def EditaCliente(request, cliente_id):
    
    cliente = CLIENTES.objects.get(id=cliente_id)

    if request.method == "POST":

        formulario = CreaCliente(request.POST)

        if formulario.is_valid():

            dato_cliente = formulario.cleaned_data

            cliente.nombre = dato_cliente["nombre"]
            cliente.apellido = dato_cliente["apellido"]
            cliente.razonSocial = dato_cliente["razonSocial"]
            cliente.direccion = dato_cliente["direccion"]
            cliente.codigoPostal = dato_cliente["codigoPostal"]
            cliente.telefono = dato_cliente["telefono"]
            cliente.eMail = dato_cliente["eMail"]
            cliente.form_pago = dato_cliente["form_pago"]
            cliente.codigo_Cliente = dato_cliente["codigo_Cliente"]
            cliente.tipo_Cliente = dato_cliente["tipo_Cliente"]
            
            cliente.save()
            
            return redirect("08_Clientes")

    formulario = CreaCliente(initial={
        
                            'nombre':cliente.nombre, 
                            'apellido':cliente.apellido, 
                            'razonSocial':cliente.razonSocial, 
                            'direccion':cliente.direccion, 
                            'codigoPostal':cliente.codigoPostal, 
                            'telefono':cliente.telefono, 
                            'eMail':cliente.eMail, 
                            'form_pago':cliente.form_pago, 
                            'codigo_Cliente':cliente.codigo_Cliente, 
                            'tipo_Cliente':cliente.tipo_Cliente
                            
                            })

    try:
            avatar = Avatar.objects.get(usuario = request.user.id)
            return render(request, "08 - AgregaCliente.html", {"form":formulario, "url": avatar.imagen.url})
    except:
        return render(request,"08 - AgregaCliente.html", {"form":formulario})
# Elimina Cliente
@login_required
def EliminaCliente(request, cliente_id):
    
    cliente = CLIENTES.objects.get(id=cliente_id)
    cliente.delete()

    return redirect("08_Clientes")
# Buscar Cliente
def BuscarCliente(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cliente = CLIENTES.objects.filter(nombre__icontains=nombre)
        return render(request,"08 - BusquedaResultado.html", {"cliente": cliente, "nombre": nombre})
    else:
        resultado = "No hay resultados"
    return HttpResponse(resultado)


# Agrega Proveedor
@login_required
def AgregaProveedor(request):
    if request.method == 'POST':
        
        formulario = CreaProveedor(request.POST)

        if formulario.is_valid():

            dato_proveedor = formulario.cleaned_data

            proveedor = PROVEEDORES(
                                    nombre = dato_proveedor["nombre"],
                                    apellido = dato_proveedor["apellido"],
                                    razonSocial = dato_proveedor["razonSocial"],
                                    direccion = dato_proveedor["direccion"],
                                    codigoPostal = dato_proveedor["codigoPostal"], 
                                    telefono = dato_proveedor["telefono"],
                                    eMail = dato_proveedor["eMail"],
                                    form_pago = dato_proveedor["form_pago"],
                                    codigo_Proveedor = dato_proveedor["codigo_Proveedor"],
                                    tipo_Proveedor = dato_proveedor["tipo_Proveedor"]
                                    )

            proveedor.save()

            return redirect("07_Proveedores")
        
        return render(request, "07 - AgregaProveedor.html", {"form":formulario})
    
    formulario = CreaProveedor()

    try:
            avatar = Avatar.objects.get(usuario = request.user.id)
            return render(request, "07 - AgregaProveedor.html", {"form":formulario, "url": avatar.imagen.url})
    except:
        return render(request, "07 - AgregaProveedor.html", {"form":formulario})
# Edita Proveedor
@login_required
def EditaProveedor(request, proveedor_id):
    
    proveedor = PROVEEDORES.objects.get(id=proveedor_id)

    if request.method == "POST":

        formulario = CreaProveedor(request.POST)

        if formulario.is_valid():

            dato_proveedor = formulario.cleaned_data

            proveedor.nombre = dato_proveedor["nombre"]
            proveedor.apellido = dato_proveedor["apellido"]
            proveedor.razonSocial = dato_proveedor["razonSocial"]
            proveedor.direccion = dato_proveedor["direccion"]
            proveedor.codigoPostal = dato_proveedor["codigoPostal"]
            proveedor.telefono = dato_proveedor["telefono"]
            proveedor.eMail = dato_proveedor["eMail"]
            proveedor.form_pago = dato_proveedor["form_pago"]
            proveedor.codigo_Proveedor = dato_proveedor["codigo_Proveedor"]
            proveedor.tipo_Proveedor = dato_proveedor["tipo_Proveedor"]
            
            proveedor.save()
            
            return redirect("07_Proveedores")

    formulario = CreaProveedor(initial={
        
                            'nombre':proveedor.nombre, 
                            'apellido':proveedor.apellido, 
                            'razonSocial':proveedor.razonSocial, 
                            'direccion':proveedor.direccion, 
                            'codigoPostal':proveedor.codigoPostal, 
                            'telefono':proveedor.telefono, 
                            'eMail':proveedor.eMail, 
                            'form_pago':proveedor.form_pago, 
                            'codigo_Proveedor':proveedor.codigo_Proveedor, 
                            'tipo_Proveedor':proveedor.tipo_Proveedor
                            
                            })

    try:
            avatar = Avatar.objects.get(usuario = request.user.id)
            return render(request, "07 - AgregaProveedor.html", {"form":formulario, "url": avatar.imagen.url})
    except:
        return render(request,"07 - AgregaProveedor.html", {"form":formulario})
# Elimina Proveedor
@login_required
def EliminaProveedor(request, proveedor_id):

    proveedor = PROVEEDORES.objects.get(id=proveedor_id)
    proveedor.delete()

    return redirect("07_Proveedores")
# Buscar Proveedor
def BuscarProveedor(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        proveedor = PROVEEDORES.objects.filter(nombre__icontains=nombre)
        return render(request,"07 - BusquedaResultado.html", {"proveedor": proveedor, "nombre": nombre})
    else:
        resultado = "No hay resultados"
    return HttpResponse(resultado)


# Agrega Producto
@login_required
def AgregaProducto(request):

    if request.method == 'POST':
        
        formulario = CreaProducto(request.POST)

        if formulario.is_valid():

            dato_producto = formulario.cleaned_data

            producto = PRODUCTO(
                                    monodroga = dato_producto["monodroga"],
                                    marca = dato_producto["marca"],
                                    presentacion = dato_producto["presentacion"],
                                    formFarmaceutica = dato_producto["formFarmaceutica"],
                                    certificado = dato_producto["certificado"], 
                                    codigoProducto = dato_producto["codigoProducto"],
                                    stock = dato_producto["stock"],
                                    )

            producto.save()

            return redirect("02_Productos")
        
        return render(request, "02 - AgregaProducto.html", {"form":formulario})
    
    formulario = CreaProducto()

    try:
            avatar = Avatar.objects.get(usuario = request.user.id)
            return render(request, "02 - AgregaProducto.html", {"form":formulario, "url": avatar.imagen.url})
    except:
        return render(request, "02 - AgregaProducto.html", {"form":formulario})
# Edita Producto
@login_required
def EditaProducto(request, producto_id):
    
    producto = PRODUCTO.objects.get(id=producto_id)

    if request.method == "POST":

        formulario = CreaProducto(request.POST)

        if formulario.is_valid():

            dato_producto = formulario.cleaned_data

            producto.monodroga = dato_producto["monodroga"]
            producto.marca = dato_producto["marca"]
            producto.presentacion = dato_producto["presentacion"]
            producto.formFarmaceutica = dato_producto["formFarmaceutica"]
            producto.certificado = dato_producto["certificado"]
            producto.codigoProducto = dato_producto["codigoProducto"]
            producto.stock = dato_producto["stock"]
            
            producto.save()
            
            return redirect("02_Productos")

    formulario = CreaProducto(initial={
        
                            'monodroga':producto.monodroga, 
                            'marca':producto.marca,
                            'presentacion':producto.presentacion, 
                            'formFarmaceutica':producto.formFarmaceutica, 
                            'certificado':producto.certificado, 
                            'codigoProducto':producto.codigoProducto, 
                            'stock':producto.stock,
                            })

    try:
            avatar = Avatar.objects.get(usuario = request.user.id)
            return render(request, "02 - AgregaProducto.html", {"form":formulario, "url": avatar.imagen.url})
    except:
        return render(request,"02 - AgregaProducto.html", {"form":formulario})
# Elimina Producto
@login_required
def EliminaProducto(request, producto_id):

    producto = PRODUCTO.objects.get(id=producto_id)
    producto.delete()

    return redirect("02_Productos")
# Buscar Producto
def BuscarProducto(request):
    if request.GET["monodroga"]:
        monodroga = request.GET["monodroga"]
        producto = PRODUCTO.objects.filter(monodroga__icontains=monodroga)
        return render(request,"02 - BusquedaResultado.html", {"producto": producto, "monodroga": monodroga})
    else:
        resultado = "No hay resultados"
    return HttpResponse(resultado)


# Agrega Empleado
@login_required
def AgregaEmpleado(request):

    if request.method == 'POST':
        
        formulario = CreaEmpleado(request.POST)

        if formulario.is_valid():

            dato_empleado = formulario.cleaned_data

            empleado = EMPLEADO(
                                    nombre = dato_empleado["nombre"],
                                    apellido = dato_empleado["apellido"],
                                    direccion = dato_empleado["direccion"],
                                    codigoPostal = dato_empleado["codigoPostal"],
                                    telefono = dato_empleado["telefono"], 
                                    eMail = dato_empleado["eMail"],
                                    puesto = dato_empleado["puesto"],
                                    cargo = dato_empleado["cargo"],
                                    horarioIngreso = dato_empleado["horarioIngreso"],
                                    horarioSalida = dato_empleado["horarioSalida"],
                                    )

            empleado.save()

            return redirect("06_Empleados")
        
        return render(request, "06 - AgregaEmpleado.html", {"form":formulario})
    
    formulario = CreaEmpleado()

    try:
            avatar = Avatar.objects.get(usuario = request.user.id)
            return render(request, "06 - AgregaEmpleado.html", {"form":formulario, "url": avatar.imagen.url})
    except:
        return render(request, "06 - AgregaEmpleado.html", {"form":formulario})
# Edita Empleado
@login_required
def EditaEmpleado(request, empleado_id):
    
    empleado = EMPLEADO.objects.get(id=empleado_id)

    if request.method == "POST":

        formulario = CreaEmpleado(request.POST)

        if formulario.is_valid():

            dato_empleado = formulario.cleaned_data

            empleado.nombre = dato_empleado["nombre"]
            empleado.apellido = dato_empleado["apellido"]
            empleado.direccion = dato_empleado["direccion"]
            empleado.codigoPostal = dato_empleado["codigoPostal"]
            empleado.telefono = dato_empleado["telefono"]
            empleado.eMail = dato_empleado["eMail"]
            empleado.puesto = dato_empleado["puesto"]
            empleado.cargo = dato_empleado["cargo"]
            empleado.horarioIngreso = dato_empleado["horarioIngreso"]
            empleado.horarioSalida = dato_empleado["horarioSalida"]
            
            empleado.save()
            
            return redirect("06_Empleados")

    formulario = CreaEmpleado(initial={
        
                            'nombre':empleado.nombre, 
                            'apellido':empleado.apellido,
                            'direccion':empleado.direccion, 
                            'codigoPostal':empleado.codigoPostal, 
                            'telefono':empleado.telefono, 
                            'eMail':empleado.eMail, 
                            'puesto':empleado.puesto,
                            'cargo':empleado.cargo,
                            'horarioIngreso':empleado.horarioIngreso,
                            'horarioSalida':empleado.horarioSalida,
                            })

    try:
            avatar = Avatar.objects.get(usuario = request.user.id)
            return render(request, "06 - AgregaEmpleado.html", {"form":formulario, "url": avatar.imagen.url})
    except:
        return render(request,"06 - AgregaEmpleado.html", {"form":formulario})
# Elimina Empleado
@login_required
def EliminaEmpleado(request, empleado_id):

    empleado = EMPLEADO.objects.get(id=empleado_id)
    empleado.delete()

    return redirect("06_Empleados")
# Buscar Empleado
def BuscarEmpleado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        empleado = EMPLEADO.objects.filter(nombre__icontains=nombre)
        return render(request,"06 - BusquedaResultado.html", {"empleado": empleado, "nombre": nombre})
    else:
        resultado = "No hay resultados"
    return HttpResponse(resultado)


# Envío de Email
def Contactar(request):
    if request.method == "POST":
        name = request.POST["nombre"]
        email = request.POST["email"]
        subject = request.POST["asunto"]
        message = request.POST["mensaje"]

        template = render_to_string('09 - Email_Template.html', {'name': name, 'email': email, 'message': message})
        
        email = EmailMessage(subject, template, settings.EMAIL_HOST_USER, ['coderpharma@gmail.com'])

        email.fail_silently = False
        email.send()
        

        messages.success(request, 'Se ha enviado su consulta')
        return redirect("09_Contacto")
    else:
        try:
            avatar = Avatar.objects.get(usuario = request.user.id)
            return render(request, "09 - Contacto.html", {"url": avatar.imagen.url})
        except:
            return render(request, "09 - Contacto.html")


#Login
def Loginview(request):

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]
            user = authenticate(username=usuario, password=psw)
            if user:
                login(request, user)
                return render(request, "01 - Inicio.html", {"mensaje": 'Bienvenido/a {usuario}'})
            else:
                return render(request, "01 - Inicio.html", {"mensaje": 'Datos incorrectos'})

        return render(request, "01 - Inicio.html")

    else:
        formulario = AuthenticationForm()
    return render(request, "09 - Login.html", {"formulario": formulario})

def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "01 - Inicio.html", {"mensaje": f'Usuario {username} creado'})

    else:
        form = UserCreationForm()

    return render(request, "10 - Regitro.html", {"formulario": form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Proveedor, Factura, Consumidor
from django.contrib import messages
from .forms import UserRegistrationForm, FacturaForm, ConsumidorForm, ProveedorForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,DeleteView



def welcome(request):
    return render(request, "home.html")
class factura_list(ListView):
    model=Factura
    template_name='vista_factura.html'
    context_object_name = 'posts'
    def get_queryset(self):
        queryset = super().get_queryset()
        campo = self.request.GET.get('campo')
        filtro = self.request.GET.get('filtro')

        if campo and filtro:
            lookup = f"{campo}__icontains"
            queryset = queryset.filter(**{lookup: filtro})

        return queryset
class factura(CreateView):
    model=Factura
    form_class=FacturaForm
    template_name='factura.html'
    success_url=reverse_lazy('vistafactura')

class eliminar_factura(DeleteView):
    model=Factura
    form_class=FacturaForm
    template_name='eliminar_factura.html'
    success_url=reverse_lazy('vistafactura')

class modificar_factura(UpdateView):
    model=Factura
    form_class=FacturaForm
    template_name='modificar_factura.html'
    success_url=reverse_lazy('vistafactura')





"""def factura(request):
    form = FacturaForm()
    if request.method == "POST":
        form = FacturaForm(request.POST)
        if form.is_valid():
            print(form)
            factura = Factura()
            factura.n_factura = form.cleaned_data['n_factura']
            factura.producto = form.cleaned_data['producto']
            factura.cantidad = form.cleaned_data['cantidad']
            factura.neto = form.cleaned_data['neto']
            factura.iva = form.cleaned_data['iva']
            factura.total = form.cleaned_data['total']
            factura.fecha_emision =form.cleaned_data['fecha_emision']
            form.save()
        else:
            print("Datos invalidos")
        return redirect('/factura')
    context = {'form': form}

    return render(request, 'factura.html', context=context)

def factura_list(request):

    filtro = request.GET.get('filtro')

    if filtro:
        facturas = Factura.objects.filter(title__icontains=filtro)
    else:
        facturas= Factura.objects.all()

    return render(
        request,
        'vista_factura.html',
        {'facturas':facturas}
    )

def eliminar_factura(request, id):
    facturas = Factura.objects.get(pk=id)
    if request.method == "POST":
             facturas.delete()
             return redirect('/vistafactura')
    
    return render(request, 'eliminar_factura.html', {'facturas': facturas})


def modificar_factura(request, id):
    facturas = Factura.objects.get(pk=id)
    form = FacturaForm(instance=facturas)
    if request.method =="POST":
        form = FacturaForm(request.POST, instance=facturas)
        form.save()
        return redirect('vistafactura')
    else:
        return render(request, 'modificar_factura.html', {'form':form})"""
    
@login_required
def consumidor(request):
    form = ConsumidorForm()
    if request.method == "POST":
        form = ConsumidorForm(request.POST)
        if form.is_valid():
            print(form)
            consumidor = Consumidor()
            consumidor.nombre = form.cleaned_data['nombre']
            consumidor.rut = form.cleaned_data['rut']
            consumidor.giro = form.cleaned_data['giro']
            consumidor.direccion = form.cleaned_data['direccion']
            consumidor.comuna= form.cleaned_data['comuna']
            consumidor.ciudad = form.cleaned_data['ciudad']
            consumidor.tipo_compra =form.cleaned_data['tipo_compra']
            form.save()
        else:
            print("Datos invalidos")
        return redirect('/consumidor')
    context = {'form': form}

    return render(request, 'consumidor.html', context=context)
@login_required
def proveedor(request):
    form = ProveedorForm()
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            print(form)
            proveedor = Proveedor()
            proveedor.rut = form.cleaned_data['rut'] 
            proveedor.razon= form.cleaned_data['razon']
            proveedor.giro = form.cleaned_data['giro']
            proveedor.direccion = form.cleaned_data['direccion']
            proveedor.email= form.cleaned_data['email']
            proveedor.telefono = form.cleaned_data['telefono']
            proveedor.tipo_venta =form.cleaned_data['tipo_venta']
            form.save()
        else:
            print("Datos invalidos")
        return redirect('/proveedor')
    context = {'form': form}

    return render(request, 'proveedor.html', context=context)

@login_required
def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            permissions = form.cleaned_data['permissions']
            username = form.cleaned_data['username']
            user.groups.add(group)
            user.user_permissions.set(permissions)
            messages.success(request, f'Usuario {username} creado exitosamente!!')
            return redirect('/home')
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'register_user.html', context)

        


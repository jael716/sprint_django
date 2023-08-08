from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission
from .models import Factura, Consumidor, Proveedor

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura 
        fields = ['n_factura','producto','cantidad','neto','iva','total','fecha_emision']
    
    def __init__(self, *args, **kwargs):
        super(FacturaForm, self).__init__(*args, **kwargs)
        form_fields = ['n_factura','producto','cantidad','neto','iva','total','fecha_emision']
        for field in form_fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class ConsumidorForm(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = ['nombre', 'rut', 'giro', 'direccion', 'comuna','ciudad','tipo_compra']

    def __init__(self, *args, **kwargs):
        super(ConsumidorForm, self).__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['rut'].widget.attrs['class'] = 'form-control'
        self.fields['giro'].widget.attrs['class'] = 'form-control'
        self.fields['direccion'].widget.attrs['class'] = 'form-control'
        self.fields['comuna'].widget.attrs['class'] = 'form-control'
        self.fields['ciudad'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_compra'].widget.attrs['class'] = 'form-control'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['rut','razon','giro', 'direccion', 'email','telefono','tipo_venta']

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)

        self.fields['rut'].widget.attrs['class'] = 'form-control'
        self.fields['razon'].widget.attrs['class'] = 'form-control'
        self.fields['giro'].widget.attrs['class'] = 'form-control'
        self.fields['direccion'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['telefono'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_venta'].widget.attrs['class'] = 'form-control'

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="Confirmacion contraseña", widget=forms.PasswordInput(attrs={"class":"form-control"}))
    date = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control"}))
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class LoginForm(forms.Form):
    nombre   = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

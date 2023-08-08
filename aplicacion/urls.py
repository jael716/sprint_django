from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from.views import factura_list,factura,modificar_factura,eliminar_factura

urlpatterns = [
    path('', views.welcome, name='home'),
    path('factura/', factura.as_view(), name="factura"), #endpoint
    path('vistafactura/',factura_list.as_view(),name="vistafactura"),
    path('eliminar_factura/<int:pk>/', eliminar_factura.as_view(), name='eliminar_factura'),
    path('modificar_factura<int:pk>/', modificar_factura.as_view(), name='modificar_factura'),
    path('consumidor/', views.consumidor, name="consumidor"),
    path('proveedor/', views.proveedor, name='proveedor'),
    path('register_user', views.register_user, name="register_user"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]

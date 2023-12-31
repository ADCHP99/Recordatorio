"""
URL configuration for compras project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio,name='inicio'),
    path('crear_cliente/',views.CrearCliente,name='CrearCliente'),
    path('listar_cliente/',views.ListarCliente,name='ListarCliente'),
    path('editar_cliente/<int:id>',views.EditarCliente,name='EditarCliente'),
    path('eliminar_cliente/<int:id>',views.EliminarCliente,name='EliminarCliente'),
    
]

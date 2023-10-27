from django.shortcuts import redirect, render

from clientes.formularioCliente import ClienteForm
from clientes.models import Cliente
# Create your views here.

def inicio (request):
    return render (request, 'index.html')

def CrearCliente(request):
    if request.method=='POST':
        clienteform=ClienteForm(request.POST)
        if clienteform.is_valid():
            clienteform.save()
            return render(request,'crear_cliente.html')
    else :
        clienteform=ClienteForm()
    return render(request, 'crear_cliente.html',{'clienteform':clienteform} )

def ListarCliente(request):
    clientes=Cliente.objects.all()
    return render(request,'listar_cliente.html',{'clientes':clientes})
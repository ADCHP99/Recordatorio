from django.shortcuts import redirect, render

from clientes.formularioCliente import ClienteForm

# Create your views here.

def inicio (request):
    return render (request, 'index.html')

def CrearCliente(request):
    if request.method=='POST':
        clienteform=ClienteForm(request.POST)
        if clienteform.is_valid():
            clienteform.save()
            return redirect('index')
    else :
        clienteform=ClienteForm()
    return render(request, 'crear_cliente.html',{'clienteform':clienteform} )
    
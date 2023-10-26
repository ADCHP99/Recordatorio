from django.forms import EmailInput, ModelForm, NumberInput
from clientes.models import Cliente


class ClienteForm (ModelForm):
    class Meta:
        model=Cliente
        fields='__all__'
        Widget={
            'correo': EmailInput(attrs={'type':'email'}),
            'edad': NumberInput(attrs={'type':'number'})
        }
        
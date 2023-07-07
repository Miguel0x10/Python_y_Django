from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona, Domicilio


# Create your views here.
#def bienvenido(request):
#    return HttpResponse('Hola mundo desde Django')

def bienvenido(request):
    #mensajes = {'msg1':'valor mensaje 1', 'msg2':'Valor mensaje 2'}
    no_personas_var= Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'no_personas':no_personas_var, 'personas':personas})


def domicilios(request):
    #mensajes = {'msg1':'valor mensaje 1', 'msg2':'Valor mensaje 2'}
    no_domicilios_var= Domicilio.objects.count()
    #personas = Persona.objects.all()
    domicilios = Domicilio.objects.order_by('id')
    return render(request, 'domicilios.html', {'no_domicilios':no_domicilios_var, 'domicilios':domicilios})

#def despedirse(request):
#    return HttpResponse('Despedida desde django')

#def contacto(request):
#    return HttpResponse('Celular: 3115689887 '\
#                       'Email: xd@xd.com')
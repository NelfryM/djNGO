from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import productos

# Create your views here.

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def Productos(request):
    #return HttpRespose(Nuestra primera vista)
    misProductos = productos.objects.all().values()
    template = loader.get_template('productos.html')
    context={
        'misProductos':misProductos,
    }
    return HttpResponse(template.render(context, request))

def Plantilla (request):
    template= loader.get_template("miPrimerTemplate.html")
    return HttpResponse(template.render())


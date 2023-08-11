from django.shortcuts import render
from django.http import HttpResponse
from inicio.forms import info_adoptantes_formulario
from inicio.forms import buscar_adoptantes_fomulario
from inicio.models import Adoptantes

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def info_adoptantes(request):
    nota = 'Gracias por elegir adoptar'
    
    if request.method == 'POST':
        formulario = info_adoptantes_formulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            adoptantes = Adoptantes(nombre=info['nombre'], edad=info['edad'], mensaje=info['mensaje'], fecha=info['fecha'])
            adoptantes.save()
            nota = 'Gracias por elegir adoptar'
        else:
            return render(request, 'inicio/info_adoptantes.html', {'formulario':formulario})
    
    formulario = info_adoptantes_formulario()
    return render(request, 'inicio/info_adoptantes.html', {'formulario': formulario})

def lista_adoptantes(request):
    return render (request, 'inicio/lista_adoptantes.html')

def sobre_nosotros(request):
    return render(request, 'inicio/sobre_nosotros.html')
 
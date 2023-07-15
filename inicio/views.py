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
            adoptantes = Adoptantes(nombre=info['nombre'], edad=info['edad'], mensaje=info['mensaje'],)
            adoptantes.save()
            nota = 'Gracias por elegir adoptar'
        else:
            return render(request, 'inicio/info_adoptantes.html', {'formulario':formulario})
    
    formulario = info_adoptantes_formulario()
    return render(request, 'inicio/info_adoptantes.html', {'formulario': formulario})

def lista_adoptantes(request):
    nota = 'Podés chequear si estás en nuestra base de datos'
    
    if request.method == 'POST':
        formulario = info_adoptantes_formulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            adoptantes = Adoptantes(nombre=info['nombre'], edad=info['edad'], mensaje=info['mensaje'],)
            adoptantes.save()
            return render(request, 'inicio/lista_adoptantes.html')
        else:
            return render(request, 'inicio/lista_adoptantes.html', {'formulario':formulario})
    
    formulario = buscar_adoptantes_fomulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
    else:
        print('Lamentablemente no estás en nuestra base de datos')
    print(nombre_a_buscar)
    return render(request, 'inicio/info_adoptantes.html', {'formulario': formulario})

 
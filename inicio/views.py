from django.shortcuts import render
from django.http import HttpResponse
from inicio.forms import info_adoptantes_formulario
from inicio.forms import buscar_adoptantes_fomulario, ModificarAdoptanteFormulario
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
            return render (request, 'inicio/lista_adoptantes.html')
            nota = 'Gracias por elegir adoptar'
        else:
            return render(request, 'inicio/info_adoptantes.html', {'formulario':formulario})
    
    formulario = info_adoptantes_formulario()
    return render(request, 'inicio/info_adoptantes.html', {'formulario': formulario})

def lista_adoptantes(request):
    formulario = Adoptantes(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        listado_adoptantes = info_adoptantes.objects.filter(nombre_icontains=nombre_a_buscar)
    else:
        ('no es válido')
    print(nombre_a_buscar)
     
    return render (request, 'inicio/lista_adoptantes.html', {'formulario': formulario, 'adoptantes':listado_adoptantes})

def sobre_nosotros(request): 
    return render(request, 'inicio/sobre_nosotros.html')

def modificar_adoptantes(request, adoptante_id):
    adoptante_a_modificar = Adoptantes.objects.get(id=adoptante_id)
    
    if request.method == 'POST':
        formulario = ModificarAdoptanteFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            adoptante_a_modificar = info['edad']
            adoptante_a_modificar.save()
            return redirect('inicio:lista_adoptantes')
    else:
        return render(request, 'inicio/modificar_adoptantes.html', {'formulario': formulario})
    
    formulario = ModificarAdoptanteFormulario()
    return render(request, 'inicio/modificar_adoptantes.html', {'formulario': formulario})
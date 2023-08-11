from django.urls import path 
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/adoptantes/', views.info_adoptantes, name='info_adoptantes'),
    path('inicio/lista_adoptantes/', views.lista_adoptantes, name='lista_adoptantes'),
    path('inicio/sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
]

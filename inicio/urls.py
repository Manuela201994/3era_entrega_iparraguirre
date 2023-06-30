from django.urls import path 
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/adoptantes/', views.info_adoptantes, name='info_adoptantes'),
    path('inicio/adoptantes/', views.lista_adoptantes, name='lista_adoptantes'),
]

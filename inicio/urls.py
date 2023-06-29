from django.urls import path 
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('info/adoptantes/', views.info_adoptantes, name='info_adoptantes')
]

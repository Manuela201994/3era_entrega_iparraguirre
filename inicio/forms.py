from django import forms

class info_adoptantes_formulario(forms.Form):
    nombre =  forms.CharField(max_length=20)
    edad = forms.CharField(max_length=3)
    telefono = forms.CharField(max_length=20)
    mensaje = forms.CharField(max_length=100)
    
class buscar_adoptantes_fomulario(forms.Form):
    nombre =  forms.CharField(max_length=20, required=False)
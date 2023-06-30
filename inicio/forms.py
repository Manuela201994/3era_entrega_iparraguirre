from django import forms

class info_adoptantes_formulario(forms.Form):
    nombre =  forms.CharField(max_length=20)
    edad = forms.IntegerField()
    mensaje = forms.DateField(required=False)
    
class buscar_adoptantes_fomulario(forms.Form):
    nombre =  forms.CharField(max_length=20, required=False)
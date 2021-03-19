"""
    Formulario usando los modelos importados
"""
from django import forms
from .models import User


class contactForm(forms.Form):
    """Formulario de contacto

    """
    subject = forms.CharField(label="Asunto:", max_length=100)
    message = forms.CharField(label="Mensaje:",widget=forms.Textarea)
    sender = forms.EmailField(label="Email: ")
    #cc_myself = forms.BooleanField(required=False)


class UserForm(forms.ModelForm):
#Crear usuario:
    
    class Meta:
        model=User
        fields=['nombre', 'apellido', 'correo']
        label={
            'nombre': "Ingresar su Nombre",
            'apellido':"Ingressar su apellido",
            'correo':"Ingresar su email"

        }



    





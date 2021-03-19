"""Formulario: cuenta de usuario
    usuario: Prueba1a
    pass: ksdPsldj8394_sjd
    pass_new: psdPsld28394_sjd1

"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, PasswordResetForm, PasswordChangeForm, 
                                        SetPasswordForm)


class LoginForm(AuthenticationForm):
#Login
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Password'

class CreateUserForm(UserCreationForm):
#Crear usuario

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='Email'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Repeat Password'


    class Meta:
        model = User
        fields = ['username','email' ,'password1','password2']
    

class PasswordChangeForm1(PasswordChangeForm):
#Modificar el password 
    
    pass


"""Recupertar Acceso a la cuenta

    -PasswordResetForm - Envía el correo de recuperación de cuenta
    -PasswordResetDoneView - Mensaje de de envío de correo satisfactorio
    -PasswordResetConfirmView - Link para resetear la cuenta
        -SetPasswordForm
    -PaaswordResetCompleteView - Password modificado

"""

class PasswordResetForm1(PasswordResetForm):
#Recuperar acceso
    
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm1, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='Email'
    
    class Meta:
        model = User
        fields = ['email']

class SetPasswordForm1(SetPasswordForm):
    
    class Meta:
        model = User
        fields=['new_password1', 'new_password2']
        label={
            'new_password1': "Nueva contraseña",
            'new_password2':"Confirmar contraseña",
        }
        widgets={
            'new_password1': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':"Ingrese la nueva contraseña"
                       }
            ),
            'new_password2': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':"Confirmar contraseña"
                       }
            ),
        }

    
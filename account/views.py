from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.http import HttpResponseRedirect
from .forms import LoginForm, CreateUserForm, PasswordResetForm1, PasswordChangeForm1, SetPasswordForm1


class LoginView(FormView):
    
    template_name="account/login.html"
    form_class=LoginForm
    success_url=reverse_lazy("dashboard")

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)
    

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)



def logoutView(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login/")


class CreateUserView(CreateView):
    template_name="account/register.html"
    form_class=CreateUserForm
    success_url=reverse_lazy("dashboard")


"""Cambiar contraseña basadas de dos maneras

    -Utilizando clases
    -Uitlizando funciones
"""
class PassworChangeView2(UpdateView):
#Modificar el password utilizando clase
 
    model=User
    form_class=PasswordChangeForm1
    template_name="account/change.html"
    #success_url=reverse_lazy("dashboard")
    
    def get(self, request, *args, **kwargs):
        form=self.form_class(user=request.user)
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form=self.form_class(user=request.user, data=request.POST )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
        

def passwordChangeView1(request):
#Cambiar contraseña, basada en funciones
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect('/dashboard/')
        else:
            form=PasswordChangeForm(user=request.user)

        return render(request,"account/change.html", {'form':form } )
    return HttpResponseRedirect('/dashboard/')



"""Recuperar Acceso a la cuenta

    -PasswordResetForm - Envía el correo de recuperación de cuenta 
    -PasswordResetDoneView - Mensaje de envío de correo satisfactorio
    -PasswordResetConfirmView - Link para resetear la cuenta
    -PaaswordResetCompleteView - Password modificado

    Importante regitrar en settings los valores de SMTP

"""
class ResetPasswordView(PasswordResetView):
#Recuperar acceso
    
    template_name="account/reset/reset.html"
    form_class=PasswordResetForm1
    from_email="noreply@gmail.com"
    success_url=reverse_lazy("password_reset_done")    

    
class PasswordResetDoneView1(PasswordResetDoneView):
    template_name="account/reset/reset_sent.html"

class PasswordResetConfirmView1(PasswordResetConfirmView):
    
    form_class=SetPasswordForm1
    template_name = 'account/reset//confirm.html'
    success_url =reverse_lazy('password_reset_complete')

class PasswordResetCompleteView1(PasswordResetCompleteView):
    template_name="account/reset/reset_complete.html"
    


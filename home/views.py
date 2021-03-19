from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm, UserForm
from .models import User



class Home(TemplateView):
    template_name='home/index.html'


def contactView(request):
    """ Formulario de contacto
       
        -Es necesario configurar las variables EMAIL en settings
    """    
    
    if request.method=="POST":
        form=contactForm(request.POST)
        if form.is_valid():
            infomation=form.cleaned_data
            #Obtener email ingresado
            infomation["message"]=infomation["message"] + "Email ingresado: "+ infomation["sender"]
            send_mail(infomation["subject"], infomation["message"], infomation["sender"],
                     [settings.EM_RECEPIENTS], )
            return render (request, "home/index.html")
    
    else:
        form=contactForm
    
    return render(request, "home/contact.html", {"form":form})




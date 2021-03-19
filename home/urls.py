from django.urls import path
from .views import Home, contactView

urlpatterns = [
    #path('', Home, name="home"),
    path('', Home.as_view(), name="home"),
    path('contacto/', contactView, name="contact"),

]

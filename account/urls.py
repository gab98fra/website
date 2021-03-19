from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (LoginView, logoutView, CreateUserView, PassworChangeView2, passwordChangeView1, 
                    ResetPasswordView, PasswordResetDoneView1, PasswordResetConfirmView1, PasswordResetCompleteView1)


urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', login_required(logoutView), name="logout"),
    path('register/', CreateUserView.as_view(), name="register"),
    path('password_change/', passwordChangeView1, name="change"),#Utilizando funciones
    path('password_change2/', PassworChangeView2.as_view(), name="change2"),#utilizando clase

    #Recuperar acceso
    path('reset_password/', ResetPasswordView.as_view(), name="reset_password"),
    path('reset_password_sent/', PasswordResetDoneView1.as_view(), name="password_reset_done"), 
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView1.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', PasswordResetCompleteView1.as_view(), name="password_reset_complete"),
    
]



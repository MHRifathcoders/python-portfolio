from os import name
from django.urls import path, include
from .views import *
from myportapp import views
# from django.contrib.auth.views import  (     
#                                     Password_Reset, 
#                                     password_reset_done,
#                                     password_reset_confirm, 
#                                 )
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', userlogin, name= 'userlogin'),
    path('register', register, name='register'),
    path('myportfolio', myportfolio, name='myportfolio'),
    path('userlogout', userlogout, name='userlogout'),
    path('my_account', my_account, name= 'my_account'),
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"), 
         name= 'reset_password'),
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
         name= 'password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
         name= 'password_reset_confirm'),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
         name= 'password_reset_complete'),
]
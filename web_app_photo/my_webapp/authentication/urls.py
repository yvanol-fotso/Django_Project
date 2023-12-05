# -*- coding: utf-8 -*-

""" authentication url configuration"""
from django.urls import path
from django.contrib.auth import views as auth_views
from django.utils.translation import gettext_lazy as _


from authentication import views as authentication_views


from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)

#pour implementer la redirection vers la page password_change_done.html



app_name = 'authentication'

urlpatterns = (

     # path(_('login/'), authentication_views.login_page, name='login

     # j'ouvre par defaut la page de login si le user n'exite pas encore sinon il doit d'abord creer son compte  NB lors de la creation du compte son  password doit contenir au moins un digit/chiffre
    path(_(''), authentication_views.login_page, name='login'),

    path(_('logout/'), authentication_views.logout_user, name='logout'),

    path('logoutGene/', LogoutView.as_view(), name='logoutGene'), #Marche

    path(_('loginGeneric/'), authentication_views.loginPageView.as_view(), name='loginGeneric'),#ne marche pas
    path(_('loginGeneric2/'),LoginView.as_view(template_name='authentication/login.html',redirect_authenticated_user=True), name='loginGeneric2'), #marche
    path(_('signup/'), authentication_views.signup_page, name='signup'),

    #NB : il faut mettre le "slash" au debut de l'url de redirection du success_url : sinon django va d'abord mettre l'url courante et en suite ajouter celle de redirection
    #si on le fait pas ie apres le success on aurait dans notre url un chemin :change-password/change-password-done/ ;ce qui ne correspond a aucun de nos chemin et conclusion URL Doesn't Exist

    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html',success_url=('/change-password-done/')),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),

    path('profile-photo/upload/', authentication_views. upload_profile_photo,name='upload_profile_photo'),

)


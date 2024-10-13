from django.urls import path

from BackEnd.Apps.Auth.Views.auth import SignUpView, SignInView, SignOutView
from BackEnd.Apps.Auth.Views.home import HomeTemplateView

app_name = 'Auth'

urlpatterns = [
  path('', HomeTemplateView.as_view(), name='home'),
  path('signup/', SignUpView.as_view(), name='signup'),  # Registro
  path('signin/', SignInView.as_view(), name='signin'),  # Inicio de sesión
  path('signout/', SignOutView.as_view(), name='signout'),  # Cierre de sesión
]

from django.urls import path

from .views import viewRegister, logIn, close_session

urlpatterns = [
    path('register', viewRegister.as_view(), name="Register"),
    path('login', logIn, name="Login"),
    path('closesess', close_session, name="CloseSession"),
]
from django.urls import path

from venomClassifierApp import views

urlpatterns = [   
    path('',views.home, name="Home"),
]
from django.urls import path

from .views import classifier

urlpatterns = [
    
    path('classifier', classifier, name="Classifier"),
]
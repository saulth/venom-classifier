from django.shortcuts import render


def home(request):

   return render(request, "venomClassifierApp/home.html")
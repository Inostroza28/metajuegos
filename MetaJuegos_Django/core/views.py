from django.shortcuts import render
from .models import Credencial


# Create your views here.
def home(request):

    return render(request, 'core/index.html')

def login(request):

    return render(request, 'core/login.html')

def register(request):
 
    return render(request, 'core/register.html')
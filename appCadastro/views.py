from django.shortcuts import render
from .models import Livro


def home(request):
    return render(request, 'home.html')


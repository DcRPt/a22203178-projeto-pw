# pwsite/views.py

from django.shortcuts import render
from datetime import datetime

def index_view(request):
    return render(request, 'pwsite/index.html',{
        'data': datetime.today()
    })

def sobre_view(request):
     return render(request, 'pwsite/sobre.html',{
        'data': datetime.today()
    })

def interesses_view(request):
     return render(request, 'pwsite/interesses.html',{
        'data': datetime.today()
    })
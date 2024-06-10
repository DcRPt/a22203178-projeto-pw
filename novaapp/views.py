# novaapp/views.py

from django.shortcuts import render
from datetime import datetime

def index_view(request):
    return render(request, 'novaapp/index.html',{
        'data': datetime.today()
    })

def sobre_view(request):
     return render(request, 'novaapp/sobre.html',{
        'data': datetime.today()
    })

def interesses_view(request):
     return render(request, 'novaapp/interesses.html',{
        'data': datetime.today()
    })
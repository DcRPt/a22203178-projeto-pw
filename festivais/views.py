from django.shortcuts import render
from .models import Localizacao, Banda, Festival

def home_view(request):
    localizacoes = Localizacao.objects.all()
    return render(request, 'festivais/index.html', {'localizacoes': localizacoes})


def festival_view(request, festival_nome):
    festival = Festival.objects.get(nome=festival_nome)
    bandas = festival.bandas.all()
    localizacao = festival.localizacao
    context = {
        'festival': festival,
        'bandas': bandas,
        'localizacao': localizacao,
    }
    return render(request, 'festivais/festival.html', context)

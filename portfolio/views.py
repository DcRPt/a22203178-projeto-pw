from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import models
import requests
from datetime import datetime

def index_view(request):
    global_id_lisboa = 1110600

    meteorologia_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_lisboa}.json'
    meteorologia_response = requests.get(meteorologia_url)
    meteorologia_response.raise_for_status()
    meteorologia_data = meteorologia_response.json()

    if not isinstance(meteorologia_data, dict) or 'data' not in meteorologia_data:
        raise ValueError("Resposta da API de previsão não é um JSON válido ou não contém 'data'")

    meteorologia_hoje = meteorologia_data['data'][0]
    meteorologia_type = meteorologia_hoje['idWeatherType']

    current_hour = datetime.now().hour
    if 6 <= current_hour < 20:
        icon_name = f'w_ic_d_{meteorologia_type:02}anim.svg'
    else:
        icon_name = f'w_ic_n_{meteorologia_type:02}anim.svg'

    icon_url = f'/static/meteo/icons/icons_ipma_weather/{icon_name}'

    context = {
        'cidade': 'Lisboa',
        'temp_minima': meteorologia_hoje['tMin'],
        'temp_maxima': meteorologia_hoje['tMax'],
        'icon_url': icon_url,
    }

    return render(request, 'portfolio/index.html', context)

def about_me_view(request):
    global_id_lisboa = 1110600

    meteorologia_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_lisboa}.json'
    meteorologia_response = requests.get(meteorologia_url)
    meteorologia_response.raise_for_status()
    meteorologia_data = meteorologia_response.json()

    if not isinstance(meteorologia_data, dict) or 'data' not in meteorologia_data:
        raise ValueError("Resposta da API de previsão não é um JSON válido ou não contém 'data'")

    meteorologia_hoje = meteorologia_data['data'][0]
    meteorologia_type = meteorologia_hoje['idWeatherType']

    current_hour = datetime.now().hour
    if 6 <= current_hour < 20:
        icon_name = f'w_ic_d_{meteorologia_type:02}anim.svg'
    else:
        icon_name = f'w_ic_n_{meteorologia_type:02}anim.svg'

    icon_url = f'/static/meteo/icons/icons_ipma_weather/{icon_name}'

    context = {
        'cidade': 'Lisboa',
        'temp_minima': meteorologia_hoje['tMin'],
        'temp_maxima': meteorologia_hoje['tMax'],
        'icon_url': icon_url,
    }

    return render(request, 'portfolio/aboutMe.html', context)

def about_view(request):
    global_id_lisboa = 1110600

    meteorologia_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_lisboa}.json'
    meteorologia_response = requests.get(meteorologia_url)
    meteorologia_response.raise_for_status()
    meteorologia_data = meteorologia_response.json()

    if not isinstance(meteorologia_data, dict) or 'data' not in meteorologia_data:
        raise ValueError("Resposta da API de previsão não é um JSON válido ou não contém 'data'")

    meteorologia_hoje = meteorologia_data['data'][0]
    meteorologia_type = meteorologia_hoje['idWeatherType']

    current_hour = datetime.now().hour
    if 6 <= current_hour < 20:
        icon_name = f'w_ic_d_{meteorologia_type:02}anim.svg'
    else:
        icon_name = f'w_ic_n_{meteorologia_type:02}anim.svg'

    icon_url = f'/static/meteo/icons/icons_ipma_weather/{icon_name}'

    context = {
        'cidade': 'Lisboa',
        'temp_minima': meteorologia_hoje['tMin'],
        'temp_maxima': meteorologia_hoje['tMax'],
        'icon_url': icon_url,
    }

    return render(request, 'portfolio/about.html', context)

def registo_view(request):
    global_id_lisboa = 1110600

    meteorologia_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_lisboa}.json'
    meteorologia_response = requests.get(meteorologia_url)
    meteorologia_response.raise_for_status()
    meteorologia_data = meteorologia_response.json()

    if not isinstance(meteorologia_data, dict) or 'data' not in meteorologia_data:
        raise ValueError("Resposta da API de previsão não é um JSON válido ou não contém 'data'")

    meteorologia_hoje = meteorologia_data['data'][0]
    meteorologia_type = meteorologia_hoje['idWeatherType']

    current_hour = datetime.now().hour
    if 6 <= current_hour < 20:
        icon_name = f'w_ic_d_{meteorologia_type:02}anim.svg'
    else:
        icon_name = f'w_ic_n_{meteorologia_type:02}anim.svg'

    icon_url = f'/static/meteo/icons/icons_ipma_weather/{icon_name}'

    context = {
        'cidade': 'Lisboa',
        'temp_minima': meteorologia_hoje['tMin'],
        'temp_maxima': meteorologia_hoje['tMax'],
        'icon_url': icon_url,
    }

    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('portfolio:login')

    return render(request, 'portfolio/registo.html', context)

def login_view(request):
    global_id_lisboa = 1110600

    meteorologia_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_lisboa}.json'
    meteorologia_response = requests.get(meteorologia_url)
    meteorologia_response.raise_for_status()
    meteorologia_data = meteorologia_response.json()

    if not isinstance(meteorologia_data, dict) or 'data' not in meteorologia_data:
        raise ValueError("Resposta da API de previsão não é um JSON válido ou não contém 'data'")

    meteorologia_hoje = meteorologia_data['data'][0]
    meteorologia_type = meteorologia_hoje['idWeatherType']

    current_hour = datetime.now().hour
    if 6 <= current_hour < 20:
        icon_name = f'w_ic_d_{meteorologia_type:02}anim.svg'
    else:
        icon_name = f'w_ic_n_{meteorologia_type:02}anim.svg'

    icon_url = f'/static/meteo/icons/icons_ipma_weather/{icon_name}'

    context = {
        'cidade': 'Lisboa',
        'temp_minima': meteorologia_hoje['tMin'],
        'temp_maxima': meteorologia_hoje['tMax'],
        'icon_url': icon_url,
    }

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('portfolio:index')
        else:
            render(request, 'portfolio/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'portfolio/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('portfolio:index')
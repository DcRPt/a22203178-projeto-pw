from django.shortcuts import render
import requests
from django.http import JsonResponse
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_PT.utf8')

def get_cities():
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(cities_url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []

def get_city_name(global_id_local):
    cidades_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(cidades_url)
    response.raise_for_status()
    cidades_data = response.json()

    for cidade in cidades_data['data']:
        if cidade['globalIdLocal'] == global_id_local:
            return cidade['local']
    return 'Cidade Desconhecida'

def lisboa_view(request):
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

    data_previsao = meteorologia_hoje['forecastDate']
    data_formatada = datetime.strptime(data_previsao, '%Y-%m-%d').strftime('%d de %B')

    cities = get_cities()

    context = {
        'cities': cities,
        'cidade': 'Lisboa',
        'temp_minima': meteorologia_hoje['tMin'],
        'temp_maxima': meteorologia_hoje['tMax'],
        'icon_url': icon_url,
        'precipita_prob': meteorologia_hoje['precipitaProb'],
        'pred_wind_dir': meteorologia_hoje['predWindDir'],
        'class_wind_speed': meteorologia_hoje['classWindSpeed'],
        'longitude': meteorologia_hoje['longitude'],
        'latitude': meteorologia_hoje['latitude'],
        'data': data_formatada,
    }
    return render(request, 'meteo/lisboa.html', context)

def previsoes_5_dias_view(request):
    global_id_local = request.GET.get('global_id_local')

    try:
        global_id_local = int(global_id_local)
    except (TypeError, ValueError):
        global_id_local = 1110600

    cidade_nome = get_city_name(global_id_local)

    meteorologia_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_local}.json'
    meteorologia_response = requests.get(meteorologia_url)
    meteorologia_response.raise_for_status()
    meteorologia_data = meteorologia_response.json()

    if not isinstance(meteorologia_data, dict) or 'data' not in meteorologia_data:
        raise ValueError("Resposta da API de previsão não é um JSON válido ou não contém 'data'")

    forecasts = []

    for meteorologia_dia in meteorologia_data['data'][:5]:
        meteorologia_type = meteorologia_dia['idWeatherType']

        current_hour = datetime.now().hour
        if 6 <= current_hour < 20:
            icon_name = f'w_ic_d_{meteorologia_type:02}anim.svg'
        else:
            icon_name = f'w_ic_n_{meteorologia_type:02}anim.svg'

        icon_url = f'/static/meteo/icons/icons_ipma_weather/{icon_name}'

        data_previsao = meteorologia_dia['forecastDate']
        data_formatada = datetime.strptime(data_previsao, '%Y-%m-%d').strftime('%d de %B')

        forecasts.append({
            'temp_minima': meteorologia_dia['tMin'],
            'temp_maxima': meteorologia_dia['tMax'],
            'icon_url': icon_url,
            'precipita_prob': meteorologia_dia['precipitaProb'],
            'pred_wind_dir': meteorologia_dia['predWindDir'],
            'class_wind_speed': meteorologia_dia['classWindSpeed'],
            'longitude': meteorologia_dia['longitude'],
            'latitude': meteorologia_dia['latitude'],
            'data': data_formatada,
        })

    cities = get_cities()

    context = {
        'cities': cities,
        'cidade': cidade_nome,
        'forecasts': forecasts,
    }
    return render(request, 'meteo/previsoes_5_dias.html', context)



def api_view(request):
    return render(request, 'meteo/api.html')

def list_cities(request):
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(cities_url)
    if response.status_code == 200:
        return JsonResponse(response.json()['data'], safe=False)
    else:
        return JsonResponse([], safe=False)


def previsao(request, global_id_local):
    previsao_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_local}.json'

    response = requests.get(previsao_url)
    response.raise_for_status()
    previsao_data = response.json()

    return JsonResponse(previsao_data)


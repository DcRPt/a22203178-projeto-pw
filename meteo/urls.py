from django.urls import path
from . import views


app_name = 'meteo'

urlpatterns = [
    path('', views.lisboa_view, name='index'),
    path('previsao/', views.previsoes_5_dias_view, name='previsao'),
    path('api/', views.api_view, name='api'),
    path('api/list_cities/', views.list_cities, name='list_cities'),
    path('api/previsao/<int:global_id_local>/', views.previsao, name='previsao'),
]
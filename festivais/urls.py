from django.urls import path
from . import views

app_name = 'festivais'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('<str:festival_nome>/', views.festival_view, name='festival_view'),
]

# project/curso/urls.py

from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.home_view, name='index'),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('curso/novo', views.novo_curso_view, name="novo_curso"),
    path('curso/<str:curso_nome>/edita', views.edita_curso_view,name="edita_curso"),
    path('curso/<str:curso_nome>/apaga', views.apaga_curso_view,name="apaga_curso"),
    path('area/novo', views.nova_area_view, name="nova_area"),
    path('area/<str:area_nome>/edita', views.edita_area_view,name="edita_area"),
    path('area/<str:area_nome>/apaga', views.apaga_area_view,name="apaga_area"),
    path('<str:curso_nome>/', views.curso_view, name='curso_view'),
    path('<str:curso_nome>/disciplina/novo', views.nova_disciplina_view, name="nova_disciplina"),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/edita', views.edita_disciplina_view,name="edita_disciplina"),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/apaga', views.apaga_disciplina_view,name="apaga_disciplina"),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/', views.disciplina_view, name='disciplina_view'),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/novo', views.novo_projeto_view, name="novo_projeto"),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/projeto/<str:projeto_nome>/edita', views.edita_projeto_view,name="edita_projeto"),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/projeto/<str:projeto_nome>/apaga', views.apaga_projeto_view,name="apaga_projeto"),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/docente/novo', views.novo_docente_view, name="novo_docente"),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/docente/<str:docente_nome>/edita', views.edita_docente_view,name="edita_docente"),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/docente/<str:docente_nome>/apaga', views.apaga_docente_view,name="apaga_docente"),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/projeto/<str:projeto_nome>/', views.projeto_view, name='projeto_view'),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/projeto/<str:projeto_nome>/linguagem/novo', views.nova_linguagem_view, name="nova_linguagem"),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/projeto/<str:projeto_nome>/linguagem/<str:linguagem_nome>/edita', views.edita_linguagem_view,name="edita_linguagem"),
    path('<str:curso_nome>/disciplina/<str:disciplina_nome>/projeto/<str:projeto_nome>/linguagem/<str:linguagem_nome>/apaga', views.apaga_linguagem_view,name="apaga_linguagem"),
]

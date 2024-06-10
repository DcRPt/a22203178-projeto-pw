from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.home_view, name='index'),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('<str:author_name>/article/<str:article_title>/', views.article_view, name='article_view'),
    path('<str:author_name>/', views.author_view, name='author_view'),
    path('autor/novo', views.novo_autor_view, name="novo_autor"),
    path('autor/<int:autor_id>/edita', views.edita_autor_view,name="edita_autor"),
    path('autor/<int:autor_id>/apaga', views.apaga_autor_view,name="apaga_autor"),
    path('artigo/novo/', views.novo_artigo_view,name="novo_artigo"),
    path('artigo/<int:artigo_id>/edita', views.edita_artigo_view,name="edita_artigo"),
    path('artigo/<int:artigo_id>/apaga', views.apaga_artigo_view,name="apaga_artigo"),
    path('artigo/<int:artigo_id>/comentario/novo/', views.novo_comentario_view, name="novo_comentario"),
    path('artigo/<int:artigo_id>/comentario/<int:comentario_id>/edita', views.edita_comentario_view, name="edita_comentario"),
    path('artigo/<int:artigo_id>/comentario/<int:comentario_id>/apaga', views.apaga_comentario_view, name="apaga_comentario"),
    path('artigo/<int:artigo_id>/rating/novo/', views.novo_rating_view, name="novo_rating"),
    path('artigo/<int:artigo_id>/rating/<int:rating_id>/edita', views.edita_rating_view, name="edita_rating"),
    path('artigo/<int:artigo_id>/rating/<int:rating_id>/apaga', views.apaga_rating_view, name="apaga_rating"),
]


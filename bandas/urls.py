from django.urls import path
from . import views


app_name = 'bandas'

urlpatterns = [
    path('', views.home_view, name='index'),
    path('css/', views.css_selectors_view, name='css'),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('banda/<str:band_name>', views.band_view, name='band_view'),
    path('album/<str:album_title>', views.album_view, name='album_view'),
    path('musica/<str:song_title>', views.song_view, name='song_view'),
    path('nova_banda', views.nova_banda_view, name="nova_banda"),
    path('banda/<str:band_name>/edita', views.edita_banda_view, name="edita_banda"),
    path('banda/<str:band_name>/apaga', views.apaga_banda_view, name="apaga_banda"),
    path('banda/<str:band_name>/novo_album', views.novo_album_view, name="novo_album"),
    path('album/<str:album_title>/edita', views.edita_album_view, name='edita_album'),
    path('album/<str:album_title>/apaga', views.apaga_album_view, name='apaga_album'),
    path('album/<str:album_title>/nova_musica', views.nova_musica_view, name='nova_musica'),
    path('musica/<str:song_title>/edita', views.edita_musica_view, name='edita_musica'),
    path('musica/<str:song_title>/apaga', views.apaga_musica_view, name='apaga_musica'),
]

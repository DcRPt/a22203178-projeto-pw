from django.shortcuts import render, redirect
from .models import Album, Band, Song
from .forms import AlbumForm, BandForm, SongForm
from django.contrib.auth import models, logout, authenticate, login
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group

def admin_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        admin_group = Group.objects.get(name='admin')
        if request.user.is_authenticated and admin_group in request.user.groups.all():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Acesso negado. Você não é um administrador.")
    return wrapped_view

def css_selectors_view(request):
    return render(request, 'bandas/html5-css.html')

def home_view(request):
    bands = Band.objects.all()

    admin_group = Group.objects.get(name='admin')
    is_admin = request.user.is_authenticated and admin_group in request.user.groups.all()

    context = {
        'bands': bands,
        'is_admin': is_admin,
    }
    return render(request, 'bandas/index.html', context)

def band_view(request, band_name):
    band = Band.objects.get(name =band_name)
    albums = Album.objects.filter(band=band)

    admin_group = Group.objects.get(name='admin')
    is_admin = request.user.is_authenticated and admin_group in request.user.groups.all()

    context = {
        'band': band,
        'albums': albums,
        'is_admin': is_admin,
    }
    return render(request, 'bandas/band.html', context)

def album_view(request, album_title):
    album = Album.objects.get(title=album_title)
    songs = Song.objects.filter(album=album)

    admin_group = Group.objects.get(name='admin')
    is_admin = request.user.is_authenticated and admin_group in request.user.groups.all()

    context = {
        'album': album,
        'songs': songs,
        'is_admin': is_admin,
    }
    return render(request, 'bandas/album.html', context)

def song_view(request, song_title):
    song = Song.objects.get(title=song_title)

    admin_group = Group.objects.get(name='admin')
    is_admin = request.user.is_authenticated and admin_group in request.user.groups.all()

    context = {
        'song': song,
        'is_admin': is_admin,
    }
    return render(request, 'bandas/song.html', context)

@login_required
@admin_required
def nova_banda_view(request):
    form = BandForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:index')

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)

@login_required
@admin_required
def edita_banda_view(request, band_name):
    banda = Band.objects.get(name=band_name)

    if request.POST:
        form = BandForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:index')

    else:
        form = BandForm(instance=banda)

    context = {'form': form, 'banda':banda}
    return render(request, 'bandas/edita_banda.html', context)

@login_required
@admin_required
def apaga_banda_view(request, band_name):
    banda = Band.objects.get(name=band_name)
    banda.delete()
    return redirect('bandas:index')

@login_required
@admin_required
def novo_album_view(request, band_name):
    banda = Band.objects.get(name=band_name)

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.banda = banda
            album.save()
            return redirect('bandas:band_view', banda.name)
    else:
        form = AlbumForm(initial={'banda': banda})

    context = {'form': form, 'banda':banda}
    return render(request, 'bandas/novo_album.html', context)

@login_required
@admin_required
def edita_album_view(request, album_title):
    album = Album.objects.get(title=album_title)
    banda = album.band

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:band_view', banda.name)
    else:
        form = AlbumForm(instance=album)

    context = {'form': form, 'album': album, 'band': banda}
    return render(request, 'bandas/edita_album.html', context)

@login_required
@admin_required
def apaga_album_view(request, album_title):
    album = Album.objects.get(title=album_title)
    banda = album.band
    album.delete()
    return redirect('bandas:band_view', banda.name)

@login_required
@admin_required
def nova_musica_view(request, album_title):
    album = Album.objects.get(title=album_title)

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            musica = form.save(commit=False)
            musica.album = album
            musica.save()
            return redirect('bandas:album_view', album.title)
    else:
        form = SongForm(initial={'album': album})

    context = {'form': form, 'album': album}
    return render(request, 'bandas/nova_musica.html', context)

@login_required
@admin_required
def edita_musica_view(request, song_title):
    musica = Song.objects.get(title=song_title)
    album = musica.album

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:album_view', album.title)
    else:
        form = SongForm(instance=musica)

    context = {'form': form, 'album': album, 'song': musica}
    return render(request, 'bandas/edita_musica.html', context)

@login_required
@admin_required
def apaga_musica_view(request, song_title):
    musica = Song.objects.get(title=song_title)
    album = musica.album
    musica.delete()
    return redirect('bandas:album_view', album.title)

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('bandas:login')

    return render(request, 'bandas/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('bandas:index')
        else:
            render(request, 'bandas/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'bandas/login.html')

def logout_view(request):
    logout(request)
    return redirect('bandas:index')
from django.shortcuts import render, redirect
from .models import Author, Article, Comment, Rating
from .forms import AutorForm, ArticleForm, CommentForm, RatingForm
from django.contrib.auth import models, logout, authenticate, login
from django.contrib.auth.decorators import login_required



def home_view(request):
    authors = Author.objects.all()
    articles = Article.objects.all()
    context = {
        'authors': authors,
        'articles': articles,
    }
    return render(request, 'artigos/index.html', context)

def author_view(request, author_name):
    author = Author.objects.get(name=author_name)
    articles = Article.objects.filter(author=author)
    context = {
        'author': author,
        'articles': articles,
    }
    return render(request, 'artigos/author.html', context)

def article_view(request, author_name, article_title):
    article = Article.objects.get(title=article_title)
    comments = Comment.objects.filter(article=article)
    ratings = Rating.objects.filter(article=article)
    context = {
        'article': article,
        'comments': comments,
        'ratings': ratings,
    }
    return render(request, 'artigos/article.html', context)

@login_required
def novo_autor_view(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('artigos:index')

    context = {'form': form}
    return render(request, 'artigos/novo_autor.html', context)

@login_required
def edita_autor_view(request, autor_id):
    autor = Author.objects.get(id=autor_id)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('artigos:index')

    context = {'form': form, 'autor': autor}
    return render(request, 'artigos/edita_autor.html', context)

@login_required
def apaga_autor_view(request, autor_id):
    autor = Author.objects.get(id=autor_id)
    autor.delete()
    return redirect('artigos:index')

@login_required
def novo_artigo_view(request, autor_id):
    autor = Author.objects.get(id=autor_id)
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.author = autor
        artigo.save()
        return redirect('artigos:article_view', author_name=autor.name, article_title=artigo.title)

    context = {'form': form}
    return render(request, 'artigos/novo_livro.html', context)

@login_required
def edita_artigo_view(request, artigo_id):
    artigo = Article.objects.get(id=artigo_id)
    form = ArticleForm(request.POST or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigos:index')

    context = {'form': form, 'artigo': artigo}
    return render(request, 'artigos/edita_artigo.html', context)

@login_required
def apaga_artigo_view(request, artigo_id):
    artigo = Article.objects.get(id=artigo_id)
    artigo.delete()
    return redirect('artigos:index')

@login_required
def novo_comentario_view(request, artigo_id):
    artigo = Article.objects.get(id=artigo_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.article = artigo
        comentario.save()
        return redirect('artigos:article_view', artigo.author.name, artigo.title)

    context = {'form': form}
    return render(request, 'artigos/novo_comentario.html', context)

@login_required
def edita_comentario_view(request, artigo_id, comentario_id):
    artigo = Article.objects.get(id=artigo_id)
    comentario = Comment.objects.get(id=comentario_id)
    form = CommentForm(request.POST or None, instance=comentario)
    if form.is_valid():
        form.save()
        return redirect('artigos:article_view', artigo.author.name, artigo.title)

    context = {'form': form, 'artigo': artigo, 'comentario': comentario}
    return render(request, 'artigos/edita_comentario.html', context)

@login_required
def apaga_comentario_view(request, artigo_id, comentario_id):
    artigo = Article.objects.get(id=artigo_id)
    comentario = Comment.objects.get(id=comentario_id)
    comentario.delete()
    return redirect('artigos:article_view', artigo.author.name, artigo.title)

@login_required
def novo_rating_view(request, artigo_id):
    artigo = Article.objects.get(id=artigo_id)
    form = RatingForm(request.POST or None)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.article = artigo
        rating.save()
        return redirect('artigos:article_view', artigo.author.name, artigo.title)

    context = {'form': form}
    return render(request, 'artigos/novo_rating.html', context)

@login_required
def edita_rating_view(request, artigo_id, rating_id):
    artigo = Article.objects.get(id=artigo_id)
    rating = Rating.objects.get(id=rating_id)
    form = RatingForm(request.POST or None, instance=rating)
    if form.is_valid():
        form.save()
        return redirect('artigos:article_view', artigo.author.name, artigo.title)

    context = {'form': form, 'rating': rating}
    return render(request, 'artigos/edita_rating.html', context)

@login_required
def apaga_rating_view(request, artigo_id, rating_id):
    artigo = Article.objects.get(id=artigo_id)
    rating = Rating.objects.get(id=rating_id)
    rating.delete()
    return redirect('artigos:article_view', artigo.author.name, artigo.title)

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('artigos:login')

    return render(request, 'artigos/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('artigos:index')
        else:
            render(request, 'artigos/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'artigos/login.html')

def logout_view(request):
    logout(request)
    return redirect('artigos:index')
from django.shortcuts import render, redirect
from .models import Curso, Disciplina, AreaCientifica, Projeto, LinguagemProgramacao, Docente
from .forms import CursoForm, DisciplinaForm, AreaForm, ProjetoForm, LinguagemForm, DocenteForm
from django.contrib.auth import models, logout, authenticate, login
from django.contrib.auth.decorators import login_required

def home_view(request):
    cursos = Curso.objects.all()
    areas = AreaCientifica.objects.all()
    context = {
        'cursos': cursos,
        'areas': areas,
    }
    return render(request, 'curso/index.html', context)

def curso_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplinas = Disciplina.objects.filter(curso=curso)
    context = {
        'curso': curso,
        'disciplinas': disciplinas,
    }
    return render(request, 'curso/curso.html', context)

def disciplina_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)
    try:
        projeto = Projeto.objects.get(disciplina=disciplina)
        linguagens = LinguagemProgramacao.objects.filter(projetos=projeto)
    except Projeto.DoesNotExist:
        projeto = None
        linguagens = None
    docentes = Docente.objects.filter(disciplinas=disciplina)
    context = {
        'projeto': projeto,
        'disciplina': disciplina,
        'curso': curso,
        'linguagens': linguagens,
        'docentes': docentes}
    return render(request, 'curso/disciplina.html', context)

def projeto_view(request, curso_nome, disciplina_nome, projeto_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)
    projeto = Projeto.objects.get(nome=projeto_nome)
    context = {
        'curso': curso,
        'disciplina': disciplina,
        'projeto': projeto,
    }
    return render(request, 'curso/projeto.html', context)

@login_required
def novo_curso_view(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso:index')

    context = {'form': form}
    return render(request, 'curso/novo_curso.html', context)

@login_required
def edita_curso_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('curso:index')

    context = {'form': form, 'curso': curso}
    return render(request, 'curso/edita_curso.html', context)

@login_required
def apaga_curso_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    curso.delete()
    return redirect('curso:index')


@login_required
def nova_area_view(request):
    form = AreaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso:index')

    context = {'form': form}
    return render(request, 'curso/nova_area_cientifica.html', context)

@login_required
def edita_area_view(request, area_nome):
    area = AreaCientifica.objects.get(nome=area_nome)
    form = AreaForm(request.POST or None, instance=area)
    if form.is_valid():
        form.save()
        return redirect('curso:index')

    context = {'form': form, 'area': area}
    return render(request, 'curso/edita_area_cientifica.html', context)

@login_required
def apaga_area_view(request, area_nome):
    area = AreaCientifica.objects.get(nome=area_nome)
    area.delete()
    return redirect('curso:index')


@login_required
def nova_disciplina_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    form = DisciplinaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso:curso_view', curso.nome)

    context = {'form': form, 'curso': curso}
    return render(request, 'curso/nova_disciplina.html', context)

@login_required
def edita_disciplina_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    form = DisciplinaForm(request.POST or None, instance=disciplina)
    if form.is_valid():
        form.save()
        return redirect('curso:curso_view', curso.nome)

    context = {'form': form, 'curso': curso,'disciplina': disciplina}
    return render(request, 'curso/edita_disciplina.html', context)

@login_required
def apaga_disciplina_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    disciplina.delete()
    return redirect('curso:curso_view', curso.nome)

@login_required
def novo_projeto_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso:disciplina_view', curso.nome, disciplina.nome)

    context = {'form': form, 'curso': curso, 'disciplina': disciplina,}
    return render(request, 'curso/novo_projeto.html', context)

@login_required
def edita_projeto_view(request, curso_nome, disciplina_nome, projeto_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    projeto = Projeto.objects.get(nome=projeto_nome)
    form = ProjetoForm(request.POST or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('curso:disciplina_view', curso.nome, disciplina.nome)

    context = {'form': form, 'curso': curso, 'disciplina': disciplina, 'projeto': projeto}
    return render(request, 'curso/edita_projeto.html', context)

@login_required
def apaga_projeto_view(request, curso_nome, disciplina_nome, projeto_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    projeto = Projeto.objects.get(nome=projeto_nome)
    projeto.delete()
    return redirect('curso:disciplina_view', curso.nome, disciplina.nome)

@login_required
def novo_docente_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    form = DocenteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso:disciplina_view', curso.nome, disciplina.nome)

    context = {'form': form, 'curso': curso, 'disciplina': disciplina}
    return render(request, 'curso/novo_docente.html', context)

@login_required
def edita_docente_view(request, curso_nome, disciplina_nome, docente_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    docente = Docente.objects.get(nome=docente_nome)
    form = DocenteForm(request.POST or None, instance=docente)
    if form.is_valid():
        form.save()
        return redirect('curso:disciplina_view', curso.nome, disciplina.nome)

    context = {'form': form, 'curso': curso, 'disciplina': disciplina, 'docente': docente}
    return render(request, 'curso/edita_docente.html', context)

@login_required
def apaga_docente_view(request, curso_nome, disciplina_nome, docente_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    docente = Docente.objects.get(nome=docente_nome)
    docente.delete()
    return redirect('curso:disciplina_view', curso.nome, disciplina.nome)


@login_required
def nova_linguagem_view(request, curso_nome, disciplina_nome, projeto_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    projeto = Projeto.objects.get(nome=projeto_nome)
    form = LinguagemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso:projeto_view', curso.nome, disciplina.nome, projeto.nome)

    context = {'form': form, 'curso': curso, 'disciplina': disciplina, 'projeto': projeto}
    return render(request, 'curso/nova_linguagem.html', context)

@login_required
def edita_linguagem_view(request, curso_nome, disciplina_nome, projeto_nome, linguagem_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    projeto = Projeto.objects.get(nome=projeto_nome)
    linguagem = LinguagemProgramacao.objects.get(nome=linguagem_nome)
    form = LinguagemForm(request.POST or None, instance=linguagem)
    if form.is_valid():
        form.save()
        return redirect('curso:projeto_view', curso.nome, disciplina.nome, projeto.nome)

    context = {'form': form, 'curso': curso, 'disciplina': disciplina, 'projeto': projeto, 'linguagem': linguagem}
    return render(request, 'curso/edita_linguagem.html', context)

@login_required
def apaga_linguagem_view(request, curso_nome, disciplina_nome, projeto_nome, linguagem_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    projeto = Projeto.objects.get(nome=projeto_nome)
    linguagem = LinguagemProgramacao.objects.get(nome=linguagem_nome)
    linguagem.delete()
    return redirect('curso:projeto_view', curso.nome, disciplina.nome, projeto.nome)

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('curso:login')

    return render(request, 'curso/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('curso:index')
        else:
            render(request, 'curso/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'curso/login.html')

def logout_view(request):
    logout(request)
    return redirect('curso:index')
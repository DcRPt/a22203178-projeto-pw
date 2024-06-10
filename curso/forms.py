from django import forms
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do curso'}),
            'apresentacao': forms.Textarea(attrs={'placeholder': 'Apresentação do curso'}),
            'objetivos': forms.Textarea(attrs={'placeholder': 'Objetivos do curso'}),
            'competencias': forms.Textarea(attrs={'placeholder': 'Competências do curso'}),
        }

class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaCientifica
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da área científica'}),
        }

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da disciplina'}),
            'ano': forms.NumberInput(attrs={'placeholder': 'Ano da disciplina'}),
            'semestre': forms.TextInput(attrs={'placeholder': 'Semestre da disciplina'}),
            'ects': forms.NumberInput(attrs={'placeholder': 'ECTS da disciplina'}),
            'curricular_unit_code': forms.TextInput(attrs={'placeholder': 'Código da unidade curricular'}),
        }

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do projeto'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Descrição do projeto'}),
            'conceitos_aplicados': forms.Textarea(attrs={'placeholder': 'Conceitos aplicados no projeto'}),
            'tecnologias_usadas': forms.Textarea(attrs={'placeholder': 'Tecnologias usadas no projeto'}),
            'video_link': forms.URLInput(attrs={'placeholder': 'Link do vídeo do projeto'}),
            'github_link': forms.URLInput(attrs={'placeholder': 'Link do GitHub do projeto'}),
        }

class LinguagemForm(forms.ModelForm):
    class Meta:
        model = LinguagemProgramacao
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da linguagem de programação'}),
        }

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do docente'}),
        }

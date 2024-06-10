from django import forms
from .models import Author, Article, Comment, Rating

class AutorForm(forms.ModelForm):
  class Meta:
    model = Author
    fields = '__all__'

    widgets = {
      'name': forms.TextInput(attrs={
                'placeholder':'Nome completo',
        }),
        'email': forms.EmailInput(attrs={
            'placeholder':'Email',
        })
    }

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = '__all__'

    labels = {
        'title': 'Título',
        'content': 'Conteúdo',
        'author': 'Autor',
        'created_at': 'Data de criação',
    }

    help_texts = {
        'created_at': 'verifique a data de criação',
    }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Digite seu comentário aqui'}),
            'comenter_name': forms.TextInput(attrs={'placeholder': 'Seu nome'}),
        }

        labels = {
            'content': 'Conteúdo do Comentário',
            'comenter_name': 'Nome do Comentador',
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'

        widgets = {
            'rating_value': forms.NumberInput(attrs={'placeholder': 'Insira sua avaliação (1-5)'}),
        }

        labels = {
            'rating_value': 'Avaliação (1-5)',
        }
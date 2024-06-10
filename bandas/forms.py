from django import forms
from .models import Band, Album, Song

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
        help_texts = {
            'name': 'Insira o nome da banda. Este é o nome pelo qual a banda é conhecida.',
            'nationality': 'País onde a banda foi originalmente formada.',
            'year_start': 'Ano em que a banda começou suas atividades.',
            'num_members': 'Quantidade atual de membros na banda.',
            'photo': 'Uma foto oficial da banda. Preferencialmente uma imagem recente.',
            'bio': 'Insira uma breve biografia da banda, com 4-5 linhas sobre sua história e estilo musical.'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome da Banda'}),
            'nationality': forms.TextInput(attrs={'placeholder': 'Nacionalidade'}),
            'year_start': forms.NumberInput(attrs={'placeholder': 'Ano de formação'}),
            'num_members': forms.NumberInput(attrs={'placeholder': 'Número de membros'}),
            'photo': forms.FileInput(attrs={'placeholder': 'Foto da Banda'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Biografia'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Título do Álbum'}),
            'band': forms.Select(attrs={'placeholder': 'Banda'}),
            'cover': forms.FileInput(attrs={'placeholder': 'Capa do Álbum'}),
            'number_of_songs': forms.NumberInput(attrs={'placeholder': 'Número de músicas'}),
            'release_year': forms.NumberInput(attrs={'placeholder': 'Ano de lançamento'}),
        }

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Título da Música'}),
            'album': forms.Select(attrs={'placeholder': 'Álbum'}),
            'lyrics': forms.Textarea(attrs={'placeholder': 'Letra da Música'}),
            'spotify_link': forms.URLInput(attrs={'placeholder': 'Link do Spotify'}),
            'duration': forms.TextInput(attrs={'placeholder': 'Duração'}),
            'biography': forms.Textarea(attrs={'placeholder': 'Biografia da Música'}),
        }

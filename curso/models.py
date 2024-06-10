from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()
    area_cientifica = models.ForeignKey('AreaCientifica', on_delete=models.CASCADE, null=True, blank=True)
    disciplinas = models.ManyToManyField('Disciplina', related_name='cursos')


    def __str__(self):
        return self.nome

class AreaCientifica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=50)
    ects = models.IntegerField()
    curricular_unit_code = models.CharField(max_length=50)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_usadas = models.TextField()
    imagem = models.ImageField(upload_to='projeto_images', null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome

class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=100)
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.nome
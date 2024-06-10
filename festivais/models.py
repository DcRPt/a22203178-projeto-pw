from django.db import models

class Localizacao(models.Model):
    cidade = models.CharField(max_length=100)

class Banda(models.Model):
    nome = models.CharField(max_length=200)
    genero = models.CharField(max_length=50)
    membros = models.PositiveIntegerField()

class Festival(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateField()
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    bandas = models.ManyToManyField(Banda)
    cartaz = models.ImageField(upload_to='cartazes', blank=True, null=True)

    def get_cartaz(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return '/media/bandas/defaultImage.jpg'
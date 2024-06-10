from django.db import models
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)

    def __str__(self):
        return f'{self.name} has the email: {self.email}'

class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f'{self.author} wrote {self.title} at {self.created_at}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    content = models.TextField()
    comenter_name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f'{self.comenter_name} wrote on {self.article} the following: {self.content[:50]}'

class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    rating_value = models.IntegerField()
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f'Rating: {self.rating_value} for {self.article}'

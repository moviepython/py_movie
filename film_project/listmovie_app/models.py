from django.db import models
from film_app.models import Cat_Movie


class List_Movies(models.Model):
    movies = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    image = models.ImageField(upload_to='listmovie')
    movie = models.ForeignKey(Cat_Movie, on_delete=models.CASCADE)
    year = models.DateField()
    desc = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=250)
    f_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100)

    def __str__(self):
        return self.movies



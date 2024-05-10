from django.db import models
from django.urls import reverse


class Cat_Movie(models.Model):
    movie_name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='movie')

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def get_url(self):
        return reverse('listmovies_by_movie', args=[self.slug])

    def __str__(self):
        return self.movie_name






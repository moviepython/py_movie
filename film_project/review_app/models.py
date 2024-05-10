from django.db import models
from django.contrib.auth.models import User
from listmovie_app.models import List_Movies


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(List_Movies,on_delete=models.CASCADE)
    review_text = models.TextField(max_length=1000)
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie} Review by {self.user.username}'
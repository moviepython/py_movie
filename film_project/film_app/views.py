from django.shortcuts import render
from .models import Cat_Movie


def movie(request):
    cat_movie = Cat_Movie.objects.all()
    context ={
        'catmovie': cat_movie
    }
    return render(request, "index.html", context)

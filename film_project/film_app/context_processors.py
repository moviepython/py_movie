from .models import Cat_Movie


def movie_link(request):
    links = Cat_Movie.objects.all
    return {'link': links}
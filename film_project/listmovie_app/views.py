from django.shortcuts import render, get_object_or_404, redirect
from .models import List_Movies
from film_app.models import Cat_Movie
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .forms import Movie_form
from review_app.models import Review

def store(request, movie_slug=None):
    movies = None
    listmovies = None
    if(movie_slug!= None):
        movies = get_object_or_404(Cat_Movie, slug=movie_slug)
        listmovies = List_Movies.objects.filter(movie=movies)
    else:
        listmovies = List_Movies.objects.all()
    context = {
        'listmovies': listmovies
    }
    return render(request, "store.html", context)


def detail_view(request, id):
    list_movie = List_Movies.objects.get(id=id)
    review = Review.objects.all()

    return render(request, "view_detail.html", {'list_movie': list_movie, 'review': review})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if password == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username Taken")
                return redirect('film_app:register')
            elif User.objects.filter(first_name=first_name).exists():
                messages.info(request, "first_name Taken")
                return redirect('film_app:register')
            elif User.objects.filter(last_name=last_name).exists():
                messages.info(request, "last_name Taken")
                return redirect('film_app:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('film_app:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                messages.success(request, "your registration is successfull")
            return redirect('/login')
        else:
            messages.info(request, "password not maching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('store')
        else:
            messages.info(request, "invalid password")
            return redirect('/')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('store')


def edit(request, edit_id):
    list_movies = List_Movies.objects.get(id=edit_id)
    form = Movie_form(instance=list_movies)
    if request.method == 'POST':
        form = Movie_form(request.POST, instance=list_movies)
        if form.is_valid():
            form.save()
            return redirect('store')
    return render(request, "edit.html", {'form': form})


def delete(request, id):
    if request.method == 'POST':
        list_movie = List_Movies.objects.get(id=id)
        list_movie.delete()
        return redirect('store')
    return render(request, "delete.html")






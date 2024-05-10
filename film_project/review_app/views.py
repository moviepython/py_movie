from django.shortcuts import render, redirect, get_object_or_404
from listmovie_app.models import List_Movies
from .forms import ReviewForm
from .models import Review
from django.contrib import messages


def review_add(request, id):
    movie = get_object_or_404(List_Movies, id=id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('store')
    else:

        initial_data = {'movie': movie}
        form = ReviewForm(initial=initial_data)

    return render(request, 'review.html', {'form': form})
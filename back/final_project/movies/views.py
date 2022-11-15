from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from .models import Movie

def index(request):
    movies = get_list_or_404(Movie)
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Movie

# Create your views here.

def home (request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render (request, 'home.html')
    #return render (request,'home.html',{'name':'Laura Sofia Aceros Monsalve'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies= Movie.objects.filter(title__icontains=searchTerm)
    else:

        movies = Movie.objects.all()
    return render(request,'home.html',{'searchTerms':searchTerm, 'movies':movies, 'range': range(1, 6),})

def rate_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        rating = int(request.POST.get('rating', 0))
        movie.rating = rating
        movie.save()
    return redirect('/')  # Cambia a tu ruta principal si es distinta

def about (request):
    #return HttpResponse('<h2>Welcome to Page About<h2>')
    return render (request,'about.html' )
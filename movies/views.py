from django.http import HttpResponse
from django.template import loader
from .models import Movie
def index(request):
    movies = Movie.objects.order_by('title')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movies}, request))

def movie(request, movie_id):
    movie = Movie.objects.get(pk = movie_id) 
    template = loader.get_template('display_movie.html')
    context = {
        'movie': movie
    }
    return HttpResponse(template.render(context, request))
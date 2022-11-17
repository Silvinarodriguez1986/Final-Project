from django.shortcuts import render

from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import loader
from movie.models import Movie
from movie.forms import MovieForm 





def get_movies(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)



def create_movie(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            data = movie_form.cleaned_data
            actual_objects = Movie.objects.filter(
                title=data["title"], description=data["description"], genre=data["genre"], duration=data["duration"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"La pelicula {data['title']} - {data['description']} - {data['genre']} - {data['duration']} ya está creado",
                )
            else:
                movie = Movie(title=data["title"], description=data["description"], genre=data["genre"], duration=data["duration"])
                movie.save()
                messages.success(
                    request,
                     f"La pelicula {data['title']} - {data['description']} - {data['genre']} - {data['duration']} creado exitosamente",
                )

            return render(
                request=request,
                context={"movies": get_movies(request)},
                template_name="movie/movie_list.html",
            )

    movie_form = MovieForm(request.POST)
    context_dict = {"form": movie_form}
    return render(
        request=request,
        context=context_dict,
        template_name="movie/movie_form.html",
        
    )

def movies(request):
    return render(
        request=request,
        context={"movies": get_movies(request)},
        template_name="movie/movie_list.html",
    )
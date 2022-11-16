from django.shortcuts import render

from movie.models import Movie

def movies(request):
    movies = Movie.objects.all()

    context_dict = {"movies": movies}

    return render(
        request=request,
        context=context_dict,
        template_name="movie/movie_list.html",
    )
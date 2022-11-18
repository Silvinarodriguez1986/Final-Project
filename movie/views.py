from django.shortcuts import render

from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import loader
from movie.models import Movie
from movie.forms import MovieForm 
from django.forms.models import model_to_dict





def get_movies(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 2)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)



def create_movie(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            data = movie_form.cleaned_data
            actual_objects = Movie.objects.filter(
                title=data["title"], genre=data["genre"], duration=data["duration"], description=data["description"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"La pelicula {data['title']} - {data['genre']} - {data['duration']} - {data['description']}  ya está creado",
                )
            else:
                movie = Movie(title=data["title"], genre=data["genre"], duration=data["duration"], description=data["description"])
                movie.save()
                messages.success(
                    request,
                     f"La pelicula {data['title']} - {data['genre']} - {data['duration']}- {data['description']}  creado exitosamente",
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



def movie_detail(request, pk: int):
    return render(
        request=request,
        context={"movie": Movie.objects.get(pk=pk)},
        template_name="movie/movie_detail.html",
    )


def movie_update(request, pk: int):
    movie = Movie.objects.get(pk=pk)

    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            data = movie_form.cleaned_data
            movie.title = data["title"]
            movie.genre = data["genre"]
            movie.duration = data["duration"]
            movie.description = data["description"]
            movie.save()

            return render(
                request=request,
                context={"movie": movie},
                template_name="movie/movie_detail.html",
            )

    movie_form = MovieForm(model_to_dict(movie))
    context_dict = {
        "movie": movie,
        "form": movie_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="movie/movie_form.html",
    )


def movie_delete(request, pk: int):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie.delete()

        movies = Movie.objects.all()
        context_dict = {"movie_list": movies}
        return render(
            request=request,
            context=context_dict,
            template_name="movie/movie_list.html",
        )

    context_dict = {
        "movie": movie,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="movie/movie_confirm_delete.html",
    )

from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from movie.models import Movie

class MovieListView(ListView):
    model = Movie
    paginate_by = 2


class MovieDetailView(DetailView):
    model = Movie
    fields = ["title", "genre", "duration", "description"]


class MovieCreateView(CreateView):
    model = Movie
    success_url = reverse_lazy("movie:movie-list")

    form_class = MovieForm
    # fields =  ["title", "genre", "duration", "description"]

    def form_valid(self, form):
        """Filter to avoid duplicate movies"""
        data = form.cleaned_data
        actual_objects = Movie.objects.filter(
            title=data["title"], genre=data["genre"], duration=data["duration"], description=data["description"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                 f"La pelicula {data['title']} - {data['genre']} - {data['duration']} - {data['description']}  ya está creado",
             
            )
            form.add_error("title", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"La pelicula {data['title']} - {data['genre']} - {data['duration']}- {data['description']}  creado exitosamente",
               
            )
            return super().form_valid(form)


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ["title", "genre", "duration", "description"]

    def get_success_url(self):
        movie_id = self.kwargs["pk"]
        return reverse_lazy("movie:movie-detail", kwargs={"pk": movie_id})


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy("movie:movie-list")









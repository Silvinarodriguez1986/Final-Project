from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from movie.forms import CommentForm
from movie.forms import MovieForm
from movie.models import Comment
from movie.models import Movie



class MovieListView(ListView):
    model = Movie
    paginate_by = 2


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie/movie_detail.html"
    fields = ["title", "genre", "duration", "description"]

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        comments = Comment.objects.filter(movie=movie).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "movie": movie,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    success_url = reverse_lazy("movie:movie-list")

    form_class = MovieForm
    # fields = ["title", "genre", "duration", "description", "image"]

    def form_valid(self, form):
        """Filter to avoid duplicate movies"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Movie.objects.filter(
            title=data["title"], genre=data["genre"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La pelicula {data['title']} - {data['genre']} ya está creado",
            )
            form.add_error("title", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Pelicula {data['title']} - {data['genre']} creado exitosamente!",
            )
            return super().form_valid(form)


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ["title", "genre", "duration", "description", "image"]

    def get_success_url(self):
        movie_id = self.kwargs["pk"]
        return reverse_lazy("movie:movie-detail", kwargs={"pk": movie_id})
    
    #def post(self):
      #  pass

class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = reverse_lazy("movie:movie-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, movie=movie
        )
        comment.save()
        return redirect(reverse("movie:movie-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        movie = self.object.movie
        return reverse("movie:movie-detail", kwargs={"pk": movie.id})












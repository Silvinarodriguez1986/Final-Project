from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from serie.forms import CommentForm
from serie.forms import SerieForm
from serie.models import Comment_serie
from serie.models import Serie

class SerieListView(ListView):
    model = Serie
    paginate_by = 3
    #template_name = "movie/movie_list.html" --> No es necesario ya que Django busca automatico el html con el nombre_list.

class SerieDetailView(DetailView):
    model = Serie
    template_name = "serie/serie_detail.html"
    fields = ["title", "genre", "duration", "description"]

    def get(self, request, pk):
        serie = Serie.objects.get(id=pk)
        comments = Comment_serie.objects.filter(serie=serie).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "serie": serie,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)


class SerieCreateView(LoginRequiredMixin, CreateView):
    model = Serie
    success_url = reverse_lazy("serie:serie-list")

    form_class = SerieForm
    # fields = ["title", "genre", "duration", "description"]

    def form_valid(self, form):
        """Filter to avoid duplicate series"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Serie.objects.filter(
            title=data["title"], genre=data["genre"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La serie {data['title']} - {data['genre']} ya está creada",
            )
            form.add_error("title", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Serie {data['title']} - {data['genre']} creada exitosamente!",
            )
            return super().form_valid(form)

class SerieUpdateView(LoginRequiredMixin, UpdateView):
    model = Serie
    fields = ["title", "genre", "duration", "description", "image"]

    def get_success_url(self):
        serie_id = self.kwargs["pk"]
        return reverse_lazy("serie:serie-detail", kwargs={"pk": serie_id})

class SerieDeleteView(LoginRequiredMixin, DeleteView):
    model = Serie
    success_url = reverse_lazy("serie:serie-list")

class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        serie = get_object_or_404(Serie, id=pk)
        comment = Comment_serie(
            text=request.POST["comment_text"], owner=request.user, serie=serie
        )
        comment.save()
        return redirect(reverse("serie:serie-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment_serie

    def get_success_url(self):
        serie = self.object.serie
        return reverse("serie:serie-detail", kwargs={"pk": serie.id})


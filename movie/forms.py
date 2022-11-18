from django import forms

from ckeditor.widgets import CKEditorWidget
from movie.models import Movie


class MovieForm(forms.Form):
    title = forms.CharField(
        label="Nombre de la pelicula",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-title",
                "placeholder": "Nombre de la pelicula",
                "required": "True",
            }
        ),
    )
    description = forms.CharField(
        label="Descripcion:",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "class": "movie-description",
                "placeholder": "Descripcion de la pelicula",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Movie
        fields = ["title", "description", "genre", "duration",]


    genre = forms.CharField(
        label="Genero de la pelicula",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-title",
                "placeholder": "Genero de la pelicula",
                "required": "True",
            }
        ),
    )
    duration = forms.IntegerField(
        label="Duracion de la pelicula",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-title",
                "placeholder": "Duracion de la pelicula",
                "required": "True",
            }
        ),
    )
  

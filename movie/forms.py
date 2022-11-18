from ckeditor.widgets import CKEditorWidget
from django import forms

from movie.models import Movie


class MovieForm(forms.ModelForm):
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


    genre = forms.CharField(
        label="Genero",
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
        label="Duracion",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-title",
                "placeholder": "Duracion de la pelicula",
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
        fields = ["title", "genre", "duration", "description"]
  

from ckeditor.widgets import CKEditorWidget
from django import forms

from movie.models import Movie


class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label="Nombre de la pelicula",
        max_length=40,
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


class CommentForm(forms.Form):
       comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )    
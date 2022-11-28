from ckeditor.widgets import CKEditorWidget
from django import forms
from serie.models import Serie

class SerieForm(forms.ModelForm):
    title = forms.CharField(
        label="Nombre de la serie",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-title",
                "placeholder": "Nombre de la serie",
                "required": "True",
            }
        ),
    )


    genre = forms.CharField(
        label="Genero",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-title",
                "placeholder": "Genero de la serie",
                "required": "True",
            }
        ),
    )
    duration = forms.IntegerField(
        label="Duracion",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-title",
                "placeholder": "Duracion de la serie",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Descripcion:",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "class": "serie-description",
                "placeholder": "Descripcion de la serie",
                "required": "True",
            }
        ),
    )
 
    image = forms.ImageField()

    class Meta:
        model = Serie
        fields = ["title", "genre", "duration", "description", "image"]


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
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField

class Movie(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False)
    genre =  models.CharField(max_length=40, null=False, blank=False)
    duration =  models.IntegerField(null=False, blank=False)
    description =  RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='movie', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        unique_together = (
            "title",
            "genre",
            "duration",
            "description",
        )
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} - {self.genre} - {self.duration} - {self.description}"


class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
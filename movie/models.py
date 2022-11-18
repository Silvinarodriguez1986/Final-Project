from django.db import models
from ckeditor.fields import RichTextField


class Movie(models.Model):
    title = models.CharField(max_length=40)
    genre =  models.CharField(max_length=40)
    duration =  models.IntegerField()
    description =  RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
   

    def __str__(self):
        return f"{self.title} - {self.genre} - {self.duration} - {self.description}"
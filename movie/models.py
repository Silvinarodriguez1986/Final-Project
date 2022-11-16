from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=40)
    description =  models.CharField(max_length=500)
    genre =  models.CharField(max_length=40)
    duration =  models.CharField(max_length=40)
    image = models.ImageField(upload_to='movie', null=True, blank=True)
    comments =  models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.genre} - {self.duration} - {self.image} - {self.comments}"
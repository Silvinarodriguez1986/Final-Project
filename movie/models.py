from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=40)
    description =  models.CharField(max_length=500)
    genre =  models.CharField(max_length=40)
    duration =  models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return f"{self.title} - {self.description} - {self.genre} - {self.duration}"
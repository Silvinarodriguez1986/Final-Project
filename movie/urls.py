from django.urls import path 

from movie import views 

app_name = "movie"
urlpatterns = [
    path("movies", views.movies, name="movie-list"),  
]

from django.urls import path 
from movie import views 

app_name = "movie"
urlpatterns = [
    path("movies/", views.MovieListView.as_view(), name="movie-list"),
    path("movie/add/", views.MovieCreateView.as_view(), name="movie-add"),
    path("movie/<int:pk>/detail/", views.MovieDetailView.as_view(), name="movie-detail"),
    path("movie/<int:pk>/update/", views.MovieUpdateView.as_view(), name="movie-update"),
    path("movie/<int:pk>/delete/", views.MovieDeleteView.as_view(), name="movie-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]



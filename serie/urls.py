from django.urls import path 
from serie import views 

app_name = "serie"
urlpatterns = [
    path("series/", views.SerieListView.as_view(), name="serie-list"),
    path("serie/add/", views.SerieCreateView.as_view(), name="serie-add"),
    path("serie/<int:pk>/detail/", views.SerieDetailView.as_view(), name="serie-detail"),
    path("serie/<int:pk>/update/", views.SerieUpdateView.as_view(), name="serie-update"),
    path("serie/<int:pk>/delete/", views.SerieDeleteView.as_view(), name="serie-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]
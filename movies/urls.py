# movies/urls.py

from django.urls import path
from .views import upload_csv, MovieListView

urlpatterns = [
    path('upload', upload_csv, name='upload_csv'), 
    path('movies', MovieListView.as_view(), name='movie_list'), # URL for CSV upload
]

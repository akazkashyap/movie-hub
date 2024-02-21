from django.urls import path
from .views import MovieViewSet, DirectorViewSet

movie_list = MovieViewSet.as_view({'get': 'list', 'post': 'create'})
movie_detail = MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})

director_list = DirectorViewSet.as_view({'get': 'list', 'post': 'create'})
director_detail = DirectorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})

urlpatterns = [
    path('', movie_list, name='movie-list'),
    path('<int:pk>/', movie_detail, name='movie-detail'),
    path('directors/', director_list, name='director-list'),
    path('directors/<int:pk>/', director_detail, name='director-detail'),
]
from rest_framework.response import Response
from rest_framework import viewsets, filters
from .serializers import MovieSerializer, DirectorSerializer
from .models import Movie, Director


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['released_at']


class DirectorViewSet(viewsets.ModelViewSet):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()
    search_fields = ['name']
    filter_backends = [filters.SearchFilter]



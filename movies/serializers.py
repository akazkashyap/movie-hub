from .models import Movie, Director
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    director_name = serializers.ReadOnlyField(source='director.name')
    url = serializers.HyperlinkedIdentityField(view_name='movie-detail', lookup_field='pk')
    director_url = serializers.HyperlinkedIdentityField(view_name='director-detail', lookup_field='pk')

    class Meta:
        model = Movie
        fields = ['id','name','url','released_at','director', 'director_name', 'director_url']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'    
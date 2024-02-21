from django.db import models

# Create your models here.

    
class Director(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    released_at = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
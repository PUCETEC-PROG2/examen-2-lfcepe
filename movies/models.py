from django.db import models

# Create your models here.
class Movie (models.Model): #clase nombre de la tabla
    title = models.CharField(max_length= 60, null=False)
    gender= models.CharField(max_length= 20, null=False)
    director = models.CharField(max_length=40, null = False)
    year = models.IntegerField(null = False)
    synopsis = models.TextField(null = False)
    
    def __str__(self) -> str:
        return self.title
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Anime(models.Model):
    title = models.CharField(max_length=100)
    description =  models.TextField(max_length=3000)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="anime_reviews"
        )
    anime_cover = models.CloudinaryField('cover', default='placeholder')
    
    class Meta:
        ordering = ["-created_on", "author"]

    def __str__(self):
        return self.title
    

class Review(models.Model):
    author = models.CharField(max_length=40, default="anonymous")
    created_on = models.DateTimeField(auto_now_add=True)
    rate_choices = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
    )
    stars = models.IntegerField(choices=rate_choices)
    review = models.TextField(max_length=4000)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return self.anime.title
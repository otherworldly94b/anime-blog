from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Anime(models.Model):
    """
    Stores a single anime entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="anime_reviews"
    )
    anime_cover = CloudinaryField('cover', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    content = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the string representation of the Anime object.
        """
        return self.title


class Review(models.Model):
    """
    Stores a single review entry related to :model:`auth.User`
    and :model:`anime_review.Anime`.
    """
    RATE_CHOICES = (
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
        (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
    )
    anime = models.ForeignKey(
        Anime, on_delete=models.CASCADE, related_name="reviews"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    stars = models.IntegerField(choices=RATE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the Review object.
        """
        return f"Review {self.body} by {self.author}"

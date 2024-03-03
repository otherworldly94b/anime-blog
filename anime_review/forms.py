from django import forms
from .models import Review


class AnimeReviewForm(forms.ModelForm):
    """
    Form for creating or updating anime reviews.
    """
    class Meta:
        model = Review
        fields = ["stars", "body"]

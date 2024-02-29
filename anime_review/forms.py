from .models import Review 
from django import forms 


class AnimeReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["stars","body"]
        
    def __init__(self, *args, **kwargs):
        review = kwargs.pop('review', None)  # Retrieve optional review object
        super().__init__(*args, **kwargs)
        if review:
            self.initial['stars'] = review.stars
            print(f"Initial stars: {self.initial['stars']}")  # Add for debugging
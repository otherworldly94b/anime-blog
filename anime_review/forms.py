from .models import Review 
from django import forms 


class AnimeReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["stars","body"]
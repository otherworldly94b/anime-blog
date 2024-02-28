from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Anime, Review
from .forms import AnimeReviewForm


class AnimeList(generic.ListView):
    queryset = Anime.objects.filter(status=1)
    template_name = "anime_review/review.html"
    paginate_by = 6


def anime_detail(request, slug):
    
    queryset = Anime.objects.filter(status=1)
    anime = get_object_or_404(queryset, slug=slug)
    reviews = anime.reviews.all().order_by("-created_on")
    review_count = anime.reviews.filter(approved=True).count()
    
    if request.method == "POST":
        anime_review_form = AnimeReviewForm(data=request.POST)
        if anime_review_form.is_valid():
            review = anime_review_form.save(commit=False)
            review.author = request.user
            review.stars = request.POST.get('stars')
            review.anime = anime
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
            )
                        
        
    anime_review_form = AnimeReviewForm()

    return render(
        request,
        "anime_review/anime_detail.html",
        {
            "anime": anime,
            "reviews": reviews,
            "review_count": review_count,
            "anime_review_form": anime_review_form,
        },
    ) 
    
    
def review_edit(request, slug, review_id):
    """
    Display an individual review for edit.

    **Context**

    ``post``
        An instance of :model:`anime_review.Anime`.
    ``review``
        A single review related to the anime.
    ``review_form``
        An instance of :form:`anime_review.AnimeReviewForm`
    """
    if request.method == "POST":

        queryset = Anime.objects.filter(status=1)
        anime = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        anime_review_form = AnimeReviewForm(data=request.POST, instance=review)

        if anime_review_form.is_valid() and review.author == request.user:
            review = anime_review_form.save(commit=False)
            review.anime = anime
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('anime_detail', args=[slug]))
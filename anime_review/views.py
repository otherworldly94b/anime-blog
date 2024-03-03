from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic import UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Anime, Review
from .forms import AnimeReviewForm


class AnimeList(generic.ListView):
    """
    View for listing anime reviews.
    """
    queryset = Anime.objects.filter(status=1)
    template_name = "anime_review/review.html"
    paginate_by = 6


def anime_detail(request, slug):
    """
    View for displaying details of a specific anime and its reviews.

    **Context**

    ``anime``
        An instance of :model:`anime_review.Anime`.
    ``reviews``
        List of reviews related to the anime.
    ``review_count``
        Number of approved reviews for the anime.
    ``anime_review_form``
        An instance of :form:`anime_review.AnimeReviewForm`.
    """
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
    View for editing an individual review.

    **Context**

    ``anime``
        An instance of :model:`anime_review.Anime`.
    ``review``
        An instance of :model:`anime_review.Review`.
    ``anime_review_form``
        An instance of :form:`anime_review.AnimeReviewForm`.
    """
    if request.method == "POST":
        queryset = Anime.objects.filter(status=1)
        anime = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        anime_review_form = AnimeReviewForm(
            data=request.POST, instance=review)

        if anime_review_form.is_valid() and review.author == request.user:
            review = anime_review_form.save(commit=False)
            review.anime = anime
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('anime_detail', args=[slug]))


def review_delete(request, slug, review_id):
    """
    View for deleting an individual review.

    **Context**

    ``anime``
        An instance of :model:`anime_review.Anime`.
    ``review``
        An instance of :model:`anime_review.Review`.
    """
    queryset = Anime.objects.filter(status=1)
    anime = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('anime_detail', args=[slug]))

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def my_anime_blog(request):
    return HttpResponse("Hello, Anime Blog!")
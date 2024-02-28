from . import views 
from django.urls import path 

urlpatterns = [
    path('', views.AnimeList.as_view(), name="review"),
    path('<slug:slug>/', views.anime_detail, name='anime_detail'),
]
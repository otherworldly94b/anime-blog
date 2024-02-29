from . import views 
from django.urls import path 

urlpatterns = [
    path('', views.AnimeList.as_view(), name="review"),
    path('<slug:slug>/', views.anime_detail, name='anime_detail'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
]
from django.contrib import admin
from django.urls import path
import review.views

app_name="review"
urlpatterns = [
    path('review_list/<int:pk>/',review.views.review, name='review'),
    path('review_list/<int:pk>/post_review/', review.views.post_review, name = 'post_review'),
]

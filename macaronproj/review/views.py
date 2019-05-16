from django.shortcuts import render, redirect
from .models import Review
from django.utils import timezone

# Create your views here.

def review(request):
    review_text = Review.objects
    return render(request, 'review.html', {'review_text': review_text})

def post_review(request):
    review = Review()
    review.post_data = timezone.datetime.now()
    review.title = request.POST['head']
    review.content = request.POST['body']
    review.save()
    return redirect('/review')
from django.shortcuts import render, redirect, render_to_response
from .models import Review
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from decimal import Decimal
# Create your views here.

def review(request):
    review_text = Review.objects
    return render(request, 'review.html', {'review_text': review_text})

def post_review(request):

    if request.method == 'POST':

        review = Review()
        '''
        conn_user = request.conn_user
        writer = conn_uesr.username
        '''
        review.post_date = timezone.datetime.now()
        review.title = request.POST['head']
        review.content = request.POST['body']
        review.rate = Decimal()

        if len(review.title) <= 0:
            messages.error(request, 'please enter your title!')
            return HttpResponseRedirect('/review')
        if len(review.content )<= 0:
            messages.error(request, 'please enter your content!')
            return HttpResponseRedirect('/review')
        review.save()
        messages.success(request, 'Review posting success!!')
        return HttpResponseRedirect('/review')
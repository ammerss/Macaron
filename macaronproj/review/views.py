from django.shortcuts import render, redirect, render_to_response, get_object_or_404, reverse
from .models import Review
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from decimal import Decimal
from store.models import Store
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def review(request, pk):
    store = get_object_or_404(Store, pk=pk)
    review_text = store.review_set.all()
    return render(request, 'review.html', {'review_text': review_text,  'store': store})

@login_required
def post_review(request, pk):

    if request.method == 'POST':

        review = Review()
        conn_user = request.user
        review.writer = conn_user.username
        review.store = get_object_or_404(Store, pk=pk)
        review.post_date = timezone.datetime.now()
        review.title = request.POST['head']
        review.content = request.POST['body']
        review.rate = Decimal()

        if len(review.title) <= 0 :
            messages.error(request, 'please enter your title!')
            return HttpResponseRedirect(reverse('review:review', args=(pk,)))
        if len(review.content) <= 0 :
            messages.error(request, 'please enter your content!')
            return HttpResponseRedirect(reverse('review:review', args=(pk,)))
        review.save()
        messages.success(request, 'Review posting success!!')
        return HttpResponseRedirect(reverse('review:review', args=(pk,)))
    
    return HttpResponseRedirect(reverse('review:review', args=(pk,)))
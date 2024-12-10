from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = request.user  # Assign the logged-in user
            review.save()
            return redirect('reviews:review_list')  # Use the namespace here
    else:
        form = ReviewForm()

    return render(request, 'reviews/submit_review.html', {'form': form})

def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')  # Get all reviews
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Review

def delete_review(request, review_id):
    # Ensure only superusers can delete reviews
    if request.user.is_superuser:
        review = get_object_or_404(Review, id=review_id)
        review.delete()
        messages.success(request, "Review deleted successfully.")
    else:
        messages.error(request, "You do not have permission to delete this review.")
    
    return redirect('reviews:review_list') 
def all_reviews(request):
    reviews = Review.objects.all().order_by('-created_at')  # Get all reviews
    return render(request, 'reviews/all_reviews.html', {'reviews': reviews})

from django.urls import path
from . import views
app_name = 'reviews'

urlpatterns = [
    path('submit/', views.submit_review, name='submit_review'),
    path('all/', views.all_reviews, name='all_reviews'),
    path('list/', views.review_list, name='review_list'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),

]

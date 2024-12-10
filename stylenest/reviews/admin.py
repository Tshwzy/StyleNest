
from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('service','review_text', 'image', 'rating')  # Customize fields to display in the admin
    search_fields = ('service','review_text', 'image', 'rating')  # Enable search by customer username or r

from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you're using Django's auth system
    service = models.CharField(max_length=255)  # Service being reviewed
    review_text = models.TextField()  # The review content
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)  # Customer uploaded image
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    rating = models.PositiveIntegerField(default=5)  # Rating (1 to 5 stars)

    def __str__(self):
        return f'{self.customer.username} review on {self.service}'

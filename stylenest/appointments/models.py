from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='subservices')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings_as_user')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, 
        choices=[
            ('Pending', 'Pending'), 
            ('Confirmed', 'Confirmed'), 
            ('Cancelled', 'Cancelled'), 
            ('Rejected', 'Rejected')
        ], 
        default='Pending'
    )
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings_as_staff')  # New field

    def __str__(self):
        return f"{self.user.username} - {self.service.name} on {self.date}"
    
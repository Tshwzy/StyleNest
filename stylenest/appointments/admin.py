from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Service, SubService, Booking

admin.site.register(Service)
admin.site.register(SubService)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'sub_service', 'date', 'time', 'status')
    list_filter = ('status', 'service', 'date')

admin.site.register(Booking, BookingAdmin)


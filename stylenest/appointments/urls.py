from django.urls import path
from . import views

urlpatterns = [
    path('user-home/dashboard/', views.dashboard_view, name='dashboard'),
    path('book/', views.make_booking, name='book'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('user-home/', views.user_home_view, name='user_home'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('staff_home/', views.staffdashboard_view, name='staff_home'),
    path('accept-appointments/', views.accept_appointments, name='accept_appointments'),
    path('edit-booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('ajax/load-subservices/', views.load_subservices, name='ajax_load_subservices'),
    path('cancel-appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('accept_appointments/', views.accept_appointments, name='accept_appointments'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('mark_done/<int:booking_id>/', views.mark_done, name='mark_done'),
]

from django.shortcuts import render, redirect
from datetime import date
from .models import Booking
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.http import JsonResponse
from .models import SubService
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages



# Dashboard view
def dashboard_view(request):
    return render(request, 'appointments/dashboard.html')

def staffdashboard_view(request):
    # Fetch confirmed bookings for the currently logged-in staff
    confirmed_bookings = Booking.objects.filter(status='Confirmed', staff=request.user)

    context = {
        'confirmed_bookings': confirmed_bookings,
    }
    return render(request, 'appointments/staff_home.html', context)




def load_subservices(request):
    service_id = request.GET.get('service_id')
    subservices = SubService.objects.filter(service_id=service_id).values('id', 'name')
    return JsonResponse(list(subservices), safe=False)


# User home page view
def user_home_view(request):
    appointments = Booking.objects.filter(user=request.user)
    context = {
        'date': date.today().strftime('%Y-%m-%d'),
        'appointments': appointments
    }
    return render(request, 'appointments/user_home.html', context)
        	


@login_required
def make_booking(request):
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Only customers reach this point, so it should be chriss
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'appointments/book.html', {'form': form})


# Staff Dashboard
@login_required
def staff_dashboard(request):
    bookings = Booking.objects.filter(staff=request.user)
    confirmed_bookings = Booking.objects.filter(staff=request.user, status='Confirmed')
    return render(request, 'appointments/staff_dashboard.html', {'bookings': bookings, 'confirmed_bookings': confirmed_bookings})

@login_required
def mark_done(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, staff=request.user)
    booking.status = 'Done'
    booking.save()
    return redirect('staff_dashboard')


# Accept Appointment Requests




@login_required
def accept_appointments(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = get_object_or_404(Booking, id=booking_id)
        
        # Only modify the staff field and status
        if booking.status == 'Pending':
            booking.status = 'Confirmed'
            booking.staff = request.user  # Assign staff
            booking.save()
        
        return redirect('staff_dashboard')
    
    elif request.method == 'GET':
        # Handle GET request to show appointment requests
        bookings = Booking.objects.filter(status='Pending')
        return render(request, 'appointments/accept_appointments.html', {'bookings': bookings})
    
    return render(request, 'appointments/accept_appointments.html')


# Edit Booking
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('staff_dashboard')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'appointments/edit_booking.html', {'form': form})


@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Booking, id=appointment_id, user=request.user)

    if appointment.status == 'Confirmed':
        appointment.status = 'Cancelled'
        appointment.save()

    return redirect('user_home')  # Redirect back to the user's homepage


def load_subservices(request):
    service_id = request.GET.get('service_id')
    subservices = SubService.objects.filter(service_id=service_id).order_by('name')
    return JsonResponse(list(subservices.values('id', 'name')), safe=False)


def booking_success(request):
    return render(request, 'appointments/booking_success.html')
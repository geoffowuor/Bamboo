from django.shortcuts import render,redirect,get_object_or_404
from .forms import  bookingForm,reserveForm
from .models import booking,reserve
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'index.html')

def booking(request):
    if request.method == 'POST':
        form = bookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.save()
            return redirect('booking_success')  
    else:
        form = bookingForm()

    return render(request, 'booking.html', {'form': form})

def reserve(request):
    if request.method == 'POST':
        form = reserveForm(request.POST)
        if form.is_valid():
            reserve = form.save(commit=False)
            reserve.save()
            return redirect('reservation_success')  
    else:
        form = reserveForm()

    return render(request, 'reserve.html', {'form': form})


def booking_success(request):
    return render(request, 'booking_success.html')

def reservation_success(request):
    return render(request, 'reservation_success.html')



#admin pannel view
def admin(request):
    return render(request, 'admin.html')



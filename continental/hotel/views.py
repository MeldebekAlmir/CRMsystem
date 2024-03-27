from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import UpdateView
from .models import *
from .forms import *

def index(request):
    return HttpResponse("Страница Continental")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def home(request):
    return render(request, 'hotel/homePage.html')

# def addbooking(request):
#     if request.method == 'POST':
#         form = AddBookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('booking')
#     else:
#         form = AddBookingForm()

# class UpdateGuest(UpdateView):
#     model = Booking
#     fields = ['room_id', 'checkin_date']
#     template_name = 'hotel/update.html'
#     success_url = reverse_lazy('home')

def housekeeping(request):
    # Рассмотреть оптимизацию подсчета данных этих

    # today = timezone.now().date()
    # now = timezone.now()
    #
    # checkouts = Booking.objects.filter(checkout_date__gte=today, checkout_date__lte=now).count()
    # checkins = Booking.objects.filter(checkin_date__gte=today, checkin_date__lte=now).count()
    # wet_cleanings = HouseKeeping.objects.filter(date__gte=today, date__lte=now, is_clean=False).count()
    #
    # data = {
    #     'checkouts': checkouts,
    #     'checkins': checkins,
    #     'wet_cleanings': wet_cleanings,
    # }
    return render(request, 'hotel/housekeeping.html')

def booking_page(request):
    return render(request, 'hotel/bookingPage.html')

def help_page(request):
    return render(request, 'hotel/helpPage.html')

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()

    return render(request, 'hotel/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))



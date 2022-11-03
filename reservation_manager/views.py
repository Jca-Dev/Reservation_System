from django.shortcuts import render
from django.views import generic
from .models import Base, Reservation
from .forms import ReservationForm
from datetime import datetime


class Homepage(generic.ListView):
    model = Base
    template_name = 'homepage.html'


def Reservations(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    return render(request, 'reservation_page.html', {'form': form})


class Menu(generic.ListView):
    model = Base
    template_name = 'menu.html'


class Errors(generic.ListView):
    model = Base
    template_name = 'error_page.html'


class Rescomp(generic.ListView):
    model = Base
    template_name = 'reservation_complete.html'

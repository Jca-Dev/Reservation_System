from django.shortcuts import render
from django.views import generic
from .models import Base


class Homepage(generic.ListView):
    model = Base
    template_name = 'base.html'


class Reservations(generic.ListView):
    model = Base
    template_name = 'reservation_page.html'


class Menu(generic.ListView):
    model = Base
    template_name = 'menu.html'


class Errors(generic.ListView):
    model = Base
    template_name = 'error_page.html'

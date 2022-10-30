from django.shortcuts import render
from django.views import generic
from .models import Base


class Homepage(generic.ListView):
    model = Base
    template_name = 'base.html'
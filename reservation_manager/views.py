from django.shortcuts import render
from django.views.generic import ListView
from .models import Base


class Homepage(ListView):
    model = Base
    template_name = 'base.html'
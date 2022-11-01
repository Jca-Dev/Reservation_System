from django.db import models
from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator
from datetime import datetime


class Base(models.Model):

    def __str__(self):
        return self.name

# ---------------------------------- Reservation -------------------------#

# Time interval hourly H = 1 hour
H = 1
DEFAULT_RESERVATION_LENGTH = H

# max PERSON capacity M = Max
M = 25
CAPACITY_REACHED_PERSON = M

# max TABLE capacity T = Max
T = 5
CAPACITY_REACHED_TABLE = T

# Dropdown list for reservation form
INTEGER_CHOICES= [tuple([x,x]) for x in range(1,25)]


class Reservation(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone_number = models.IntegerField()
    date_time = models.DateTimeField(datetime)
    party_size = models.IntegerField()


class Meta:
    ordering = ['-date_time']


def __str__(self):
    return self.name

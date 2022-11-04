from django.db import models
import datetime


class Base(models.Model):

    def __str__(self):
        return self.name


# ---------------------------------- Reservation -------------------------#
# Time interval hourly H = 1 hour
H = 1
DEFAULT_RESERVATION_LENGTH = H

# max PERSON capacity M = Max
M = 25
CAPACITY_REACHED = M

# Dropdown list for reservation form
INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 26)]


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    party_size = models.CharField(max_length=2, choices=INTEGER_CHOICES)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.name

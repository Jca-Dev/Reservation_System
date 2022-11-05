from django.db import models
from datetime import datetime, timedelta


class Base(models.Model):

    def __str__(self):
        return self.name


# ---------------------------------- Reservation -------------------------#
max_seats = 25


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField(error_messages={'invalid': 'Please enter a valid phone number'})
    party_size = models.IntegerField()
    date_time = models.DateTimeField()

    def __str__(self):
        return self.name

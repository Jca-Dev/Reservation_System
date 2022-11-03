from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class admin_display(admin.ModelAdmin):

    list_display = ['name', 'date_time']
    list_filter = ['name', 'date_time']
    search_fields = ['name', 'date_time']

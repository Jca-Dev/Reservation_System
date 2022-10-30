from . import views
from django.urls import path


urlpatterns = [
    path('', views.Homepage.as_view(), name='home'),
    path('/reservation_page', views.Reservations.as_view(), name='reservations'),
    path('/menu', views.Menu.as_view(), name='menu'),
]

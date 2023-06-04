from django.urls import path
from . import views

urlpatterns = [
    path('saykat/bookings', views.bookings, name='saykat'),
]
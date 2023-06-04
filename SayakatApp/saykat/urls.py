from django.urls import path
from . import views

urlpatterns = [
    path('saykat/bookings', views.bookings, name='saykat'),
    path('saykat/bookings/add', views.add_bookings, name='saykat'),
]
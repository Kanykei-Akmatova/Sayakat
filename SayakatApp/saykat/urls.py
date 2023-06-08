from django.urls import path
from . import views

urlpatterns = [
    path('bookings/list', views.bookings, name='saykat-bookings-list'),
    path('bookings/add', views.add_bookings, name='saykat-bookings-add'),
]
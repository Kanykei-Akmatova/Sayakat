from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='saykat-bookings-list'),
    path('bookings/list', views.bookings, name='saykat-bookings-list'),
    path('bookings/add', views.add_bookings, name='saykat-bookings-add'),
    path('bookings/delete/<int:booking_id>', views.delete_bookings, name='saykat-bookings-delete'),
    path('packages/list', views.packages, name='saykat-packages-list'),
]
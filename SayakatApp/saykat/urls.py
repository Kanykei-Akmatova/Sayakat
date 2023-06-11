from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='saykat-home'),
    path('bookings/list', login_required(views.bookings), name='saykat-bookings-list'),
    path('bookings/add', login_required(views.add_bookings), name='saykat-bookings-add'),
    path('bookings/delete/<int:booking_id>', login_required(views.delete_bookings), name='saykat-bookings-delete'),
    path('packages/list', views.packages, name='saykat-packages-list'),
]
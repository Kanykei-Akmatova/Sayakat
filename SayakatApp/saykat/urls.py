from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.bookings, name='home'),
    path('bookings/list', views.bookings, name='saykat-bookings-list'),
    path('bookings/add', views.add_bookings, name='saykat-bookings-add'),
    path('bookings/delete/<int:booking_id>', views.delete_bookings, name='saykat-bookings-delete'),
    path('packages/list', views.packages, name='saykat-packages-list'),
    path('register', views.register, name='saykat-register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='saykat-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='saykat-logout'),
]
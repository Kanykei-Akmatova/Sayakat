from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='saykat-register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='saykat-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='saykat-logout'),
]
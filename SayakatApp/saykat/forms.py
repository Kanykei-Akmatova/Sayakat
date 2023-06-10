from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookingForm(forms.Form):
    name = forms.CharField(required=True, max_length=50)
    description = forms.CharField(required=True, max_length=255)
    date = forms.DateField(required=True)
    package = forms.IntegerField(required=True)
    customer = forms.IntegerField(required=True)


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

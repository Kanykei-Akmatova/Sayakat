from django import forms


class BookingForm(forms.Form):
    name = forms.CharField(required=True, max_length=50)
    description = forms.CharField(required=True, max_length=255)
    date = forms.DateField(required=True)
    package = forms.IntegerField(required=True)
    customer = forms.IntegerField(required=True)

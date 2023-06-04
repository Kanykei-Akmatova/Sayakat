from django.contrib import admin
from .models import Customer, Hotel, Flight, Package, Booking

# Register your models here.
admin.site.register(Customer)
admin.site.register(Hotel)
admin.site.register(Flight)
admin.site.register(Package)
admin.site.register(Booking)
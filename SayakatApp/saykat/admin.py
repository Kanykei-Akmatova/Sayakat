from django.contrib import admin
from .models import Hotel, Flight, Package, Booking

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Flight)
admin.site.register(Package)
admin.site.register(Booking)
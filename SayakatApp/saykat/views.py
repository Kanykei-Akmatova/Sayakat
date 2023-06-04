from django.http import HttpResponse
from django.template import loader
from .models import Booking, Package


def bookings(request):
    bookings_list = Booking.objects.all()

    template = loader.get_template('bookings_list.html')
    context = {
        'bookings_list': bookings_list,
    }
    return HttpResponse(template.render(context, request))


def add_bookings(request):
    package_list = Package.objects.all()

    template = loader.get_template('bookings_add.html')
    context = {
        'customer': 1,
        'package_list': package_list,
    }
    return HttpResponse(template.render(context, request))

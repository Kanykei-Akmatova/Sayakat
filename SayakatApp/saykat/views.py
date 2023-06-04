from django.http import HttpResponse
from django.template import loader
from .models import Booking


def bookings(request):
    bookings_list = Booking.objects.all()

    template = loader.get_template('bookings_list.html')
    context = {
        'bookings_list': bookings_list,
    }
    return HttpResponse(template.render(context, request))

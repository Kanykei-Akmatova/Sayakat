from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from werkzeug.utils import redirect

from .forms import BookingForm
from .models import Booking, Package, Customer


def bookings(request):
    bookings_list = Booking.objects.all()

    template = loader.get_template('bookings_list.html')
    context = {
        'bookings_list': bookings_list,
    }
    return HttpResponse(template.render(context, request))


def add_bookings(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            package = Package.objects.get(id=form.cleaned_data['package'])
            customer = Customer.objects.get(id=form.cleaned_data['customer'])

            # Create and save the model instance
            booking = Booking(name=form.cleaned_data['name'],
                              description=form.cleaned_data['description'],
                              date=form.cleaned_data['date'],
                              package=package,
                              customer=customer)
            booking.save()
            # return HttpResponse("add_bookings successfully")
            return HttpResponseRedirect("/bookings/list")
            return redirect('/new/path/')
        else:
            errors = form.errors
            # You can iterate over the errors for each field
            for field, error_list in errors.items():
                print(field, error_list)
            return HttpResponse("Not valid form")
    else:
        package_list = Package.objects.all()

        template = loader.get_template('bookings_add.html')
        context = {
            'customer': 1,
            'package_list': package_list,
        }
        return HttpResponse(template.render(context, request))

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User

from .forms import BookingForm
from .models import Booking, Package


def index(request):
    packages_list = Package.objects.all()

    template = loader.get_template('index.html')
    context = {
        'packages_list': packages_list,
        'user_id': request.user.id
    }
    return HttpResponse(template.render(context, request))


def bookings(request):
    try:
        customer_id = request.user.id
        bookings_list = Booking.objects.filter(customer_id=customer_id)

        print(customer_id)

        template = loader.get_template('bookings_list.html')
        context = {
            'bookings_list': bookings_list,
        }
        return HttpResponse(template.render(context, request))
    except Booking.DoesNotExist:
        template = loader.get_template('bookings_list.html')
        context = {
            'bookings_list': [],
        }
        return HttpResponse(template.render(context, request))


def add_bookings(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            customer_id = request.user.id
            print(customer_id)
            customer = User.objects.get(id=customer_id)
            package = Package.objects.get(id=form.cleaned_data['package'])

            # Create and save the model instance
            booking = Booking(name=form.cleaned_data['name'],
                              description=form.cleaned_data['description'],
                              date=form.cleaned_data['date'],
                              package=package,
                              customer=customer)
            booking.save()
            return HttpResponseRedirect("/bookings/list")
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


def delete_bookings(request, booking_id):
    Booking.objects.get(id=booking_id).delete()
    return HttpResponseRedirect("/bookings/list")


def packages(request):
    packages_list = Package.objects.all()

    template = loader.get_template('packages_list.html')
    context = {
        'packages_list': packages_list,
    }
    return HttpResponse(template.render(context, request))

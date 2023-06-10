from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import UserRegistrationForm, BookingForm
from .models import Booking, Package, Customer
from django.contrib import messages


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


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return HttpResponseRedirect('login')
    else:
        form = UserRegistrationForm()

    template = loader.get_template('register.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))
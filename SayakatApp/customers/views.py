from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader

from .forms import UserRegistrationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return HttpResponseRedirect('/login')
    else:
        form = UserRegistrationForm()

    template = loader.get_template('register.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

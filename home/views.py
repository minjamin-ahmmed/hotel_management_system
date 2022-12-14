from django.shortcuts import render, HttpResponse, redirect
from home.Registration import RegistrationForm
from .forms import CustomerRegistrationForm
from django.views import View
from django.contrib import messages


# Create your views here.

def home_view(request):
    return render(request, 'Home.html')


def about(request):
    return render(request, 'About.html')


def contacts(request):
    return render(request, 'Contacts.html')


def gallery(request):
    return render(request, 'Gallery.html')


def meetingandevents(request):
    return render(request, 'Meeting and Events.html')


def recreation(request):
    return render(request, 'Recreation.html')


def restaurant(request):
    return render(request, 'Restaurant.html')


def accomodation(request):
    return render(request, 'Accomodation.html')


def view(request):
    return render(request, 'view.html')


def register(request):
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if (form.is_valid()):
            form.save()
        return redirect('http://127.0.0.1:8000/')

    form = RegistrationForm()
    context = {
        'register_form': form,
    }
    return render(request, 'Registration.html', context)


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'Registration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'Registration.html', {'form': form})

from django.shortcuts import render
from django.views import View
from .models import Institution, Donation, Category

# Create your views here.

class LandingPage(View):
    def get(self, request):
        bags = Donation.objects.all().count()
        supported = Institution.objects.all().count()
        ctx = {
            "bags": bags,
            "supported": supported
        }
        return render(request, "index.html", ctx)


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class Register(View):
    def get(self, request):
        return render(request, "register.html")

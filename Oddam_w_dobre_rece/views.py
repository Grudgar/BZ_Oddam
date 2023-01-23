from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Institution, Donation, Category
from django.contrib.auth.models import User

# Create your views here.


class LandingPage(View):
    def get(self, request):
        bags = Donation.objects.all().count()
        supported = Institution.objects.all().count()
        fundations = Institution.objects.filter(type=1)
        ngos = Institution.objects.filter(type=2)
        local_collects = Institution.objects.filter(type=3)
        try:
            user = User.objects.get(username=request.user)
        except Exception:
            user = None
        ctx = {
            "bags": bags,
            "supported": supported,
            "fundations": fundations,
            "ngos": ngos,
            "local_collects": local_collects,
            "user": user,
        }
        return render(request, "index.html", ctx)


class AddDonation(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            category = Category.objects.all()
            institutions = Institution.objects.all()
            ctx = {
                "user": user,
                "category": category,
                "institutions": institutions
            }
            return render(request, "form.html", ctx)
        else:
            return render(request, "login.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        check_user = User.objects.get(username=username)
        if user is not None:
            login(request, user)
            return redirect('landing-page')
        elif check_user is None:
            return redirect('register')
        else:
            response = HttpResponse(f'Błąd logowania! Nieprawidłowe hasło bądź e-mail!')
            return response


class Register(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        username = request.POST.get('email')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        password = request.POST.get('password')
        check_password = request.POST.get('password2')
        if password == check_password:
            u = User()
            u.username = username
            u.first_name = name
            u.last_name = surname
            u.email = username
            u.set_password(password)
            u.save()
            return render(request, "login.html")
        else:
            msg = "Podano dwa różne hasła, sprawź co wpisałeś/-aś!"
            return render(request, "register.html", context={'msg': msg})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('landing-page')


class UserPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            try:
                donations = Donation.objects.filter(user_id=user)
            except Exception:
                donations = None
            ctx = {
                "user": user,
                "donations": donations,
            }
            return render(request, 'user_page.html', ctx)
        else:
            return render(request, 'login')

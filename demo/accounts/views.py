from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        #first is from the model, second one is the one you're passing
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'ten nick juz istnieje')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'ten email juz istnieje')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'hasla sie nie zgadzaja')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'niepoprawny login lub hasło')
            return redirect('login')
    else:
        messages.info(request,'rejestracja udana. teraz sie zaloguj')
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

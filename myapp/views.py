from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Feature


# Create your views here.
def index(request):
    features = Feature.objects.all()
    context = {'features': features}

    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already used")
                redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('signin')
        else:
            messages.info(request, "Password not the same")
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials are Invalid')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('/')


def counter(request):
    words = request.POST.get('text', '')
    # here split method gives the array
    total_words = len(words.split())
    print(total_words, words)
    context = {
        'total': total_words,
        'text': words,
    }
    return render(request, 'counter.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Meal_Plan, Day

# Create your views here.
def homePage(request):
    context = {}
    if request.user.is_authenticated:
        try:
            meal_plan = Meal_Plan.objects.get(user_id=request.user)
            days = Day.objects.filter(meal_plan=meal_plan)
            context = {'meal_plan': meal_plan, 'days': days}
        except:
            messages.error(request, 'Create your meal plan!')
                
    return render(request, 'base/home.html', context)

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home-page')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request, 'Username or password are not correct!')

    context = {'page': page}
    return render(request, 'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home-page')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username  = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request, 'An error occured during registration!')

    context ={'form': form}
    return render(request, 'base/login_register.html', context)
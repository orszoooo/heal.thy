from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Meal_Plan, Day, Meal, Meal_Time
from .forms import MealForm, MealPlanForm

# Create your views here.
def homePage(request):
    context = {}
    if request.user.is_authenticated:
        try:
            meal_plan = Meal_Plan.objects.get(user_id=request.user, is_active=True)
            days = Day.objects.filter(meal_plan=meal_plan)
            context = {'meal_plan': meal_plan, 'days': days}
        except:
            messages.error(request, "Please create your meal plan!")
            messages.error(request, "If you have plan already, select active plan. You can do it in profile tab.")
           
    return render(request, 'base/home.html', context)

def recipesPage(request):
    recipes = True
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    recipes_set = Meal.objects.filter(
        Q(name__icontains=q) |
        Q(category__name__icontains=q) |
        Q(author__username__icontains=q)|
        Q(description__icontains=q)
    )
    meal_times = Meal_Time.objects.all()

    context = {'recipes':recipes, 'recipes_set':recipes_set, 'meal_times': meal_times}
    return render(request, 'base/home.html', context)

@login_required(login_url='login-page')
def createMeal(request):
    form = MealForm()

    if request.method == 'POST':
        form = MealForm(request.POST)

        if form.is_valid():
            meal = form.save(commit=False)
            meal.author = request.user
            meal.save()
            return redirect('home-page')

    context = {'form': form}
    return render(request, 'base/meal_form.html', context)
    
@login_required(login_url='login-page')
def editMeal(request, pk):
    meal = Meal.objects.get(id=pk)
    form = MealForm(instance=meal)

    if request.user != meal.author:
        return HttpResponse("You are not allowed to edit recipe made by someone else!")

    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)

        if form.is_valid():
            form.save()
            return redirect('recipe-page')
    context = {'form': form}
    return render(request, 'base/meal_form.html', context)

@login_required(login_url='login-page')
def deleteMeal(request, pk):
    meal = Meal.objects.get(id=pk)

    if request.user != meal.author:
        return HttpResponse("You are not allowed to delete recipe made by someone else!")
    
    if request.method == 'POST':
        meal.delete()
        return redirect('recipe-page')

    return render(request, 'base/delete.html', {'obj': meal})

@login_required(login_url='login-page')
def createMealPlan(request):
    form = MealPlanForm()

    if request.method == 'POST':
        form = MealPlanForm(request.POST)

        if form.is_valid():
            meal_plan = form.save(commit=False)
            meal_plan.user_id = request.user
            meal_plan.save()
            return redirect('home-page')

    context = {'form': form}
    return render(request, 'base/meal_plan_form.html', context)

@login_required(login_url='login-page')
def editMealPlan(request, pk):
    meal_plan = Meal_Plan.objects.get(id=pk)
    form = MealPlanForm(instance=meal_plan)

    if request.user != meal_plan.user_id:
        return HttpResponse("You are not allowed to edit recipe made by someone else!")

    if request.method == 'POST':
        form = MealPlanForm(request.POST, instance=meal_plan)
        if form.is_valid():
            form.save()
            return redirect('profile-page')
    context = {'form':form}
    return render(request, 'base/meal_plan_form.html', context)

@login_required(login_url='login-page')
def activateMealPlan(request, pk):
    meal_plan = Meal_Plan.objects.get(id=pk)
    form = MealPlanForm(instance=meal_plan)

    if request.user != meal_plan.user_id:
        return HttpResponse("You are not allowed to edit recipe made by someone else!")
    else:
        plan = form.save(commit=False)
        plan.is_active = True
        plan.save()

    return redirect('profile-page')

@login_required(login_url='login-page')
def deactivateMealPlan(request, pk):
    meal_plan = Meal_Plan.objects.get(id=pk)
    form = MealPlanForm(instance=meal_plan)

    if request.user != meal_plan.user_id:
        return HttpResponse("You are not allowed to edit recipe made by someone else!")
    else:
        plan = form.save(commit=False)
        plan.is_active = False
        plan.save()

    return redirect('profile-page')

@login_required(login_url='login-page')
def deleteMealPlan(request, pk):
    meal_plan = Meal_Plan.objects.get(id=pk)

    if request.user != meal_plan.user_id:
        return HttpResponse("You are not allowed to delete recipe made by someone else!")
    
    if request.method == 'POST':
        meal_plan.delete()
        return redirect('profile-page')

    return render(request, 'base/delete.html', {'obj': meal_plan})

@login_required(login_url='login-page')
def profilePage(request):
    meal_plans = Meal_Plan.objects.filter(user_id=request.user)
    active_plans = meal_plans.filter(is_active = True).count()
    context = {'meal_plans': meal_plans, 'active_plans': active_plans}
    
    return render(request, 'base/profile.html', context)

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
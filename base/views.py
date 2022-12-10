from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Meal_Plan, Menu, Meal, Meal_Time
from .forms import MealForm, MealPlanForm, MenuForm, RegisterUserForm

# Create your views here.
def homePage(request):
    inspirations = Meal.objects.all()
    context = {'inspirations': inspirations}

    if request.user.is_authenticated:
        try:
            meal_plan = Meal_Plan.objects.get(user_id=request.user, is_active=True)
            menus = Menu.objects.filter(meal_plan=meal_plan)
            context.update({'meal_plan': meal_plan, 'menus': menus})
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
        form = MealForm(request.POST,request.FILES)

        if form.is_valid():
            meal = form.save(commit=False)
            meal.author = request.user
            meal.description_short = meal.description[0:50]
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
        form = MealForm(request.POST, request.FILES, instance=meal)

        if form.is_valid():
            meal = form.save(commit=False)
            meal.description_short = meal.description[0:50]
            meal.save()
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
    meal_plan_form = MealPlanForm()
    menu_form = MenuForm()
    context = {'meal_plan_form': meal_plan_form, 'menu_form': menu_form}

    try:
        meal_plan = Meal_Plan.objects.get(user_id=request.user, is_active = True)
        context.update({'meal_plan': meal_plan})
    except:
        messages.error(request, "You have plans assigned. Select active plan. ")
        messages.error(request, "If you want you can add new plan below.")
        
    if request.method == 'POST':
        meal_plan_form = MealPlanForm(request.POST)

        if meal_plan_form.is_valid():
            meal_plan = meal_plan_form.save(commit=False)
            meal_plan.user_id = request.user
            meal_plan.save()
            return redirect('create-plan')

        menu_form = MenuForm(request.POST)

        if menu_form.is_valid():
            menu = menu_form.save(commit=False)
            menu.meal_plan = meal_plan
            menu.save()
            return redirect('create-plan')

    return render(request, 'base/meal_plan.html', context)

@login_required(login_url='login-page')
def editMealPlan(request, pk):
    meal_plan = Meal_Plan.objects.get(id=pk)
    meal_plan_form = MealPlanForm(instance=meal_plan)

    if request.user != meal_plan.user_id:
        return HttpResponse("You are not allowed to edit recipe made by someone else!")

    if request.method == 'POST':
        meal_plan_form = MealPlanForm(request.POST, instance=meal_plan)
        if meal_plan_form.is_valid():
            meal_plan_form.save()
            return redirect('profile-page')
    context = {'meal_plan_form': meal_plan_form}
    return render(request, 'base/meal_plan.html', context)

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
def addMenu(request, pk):
    recipe = Meal.objects.get(id=pk)
    menu_form = MenuForm()
    menu_form.initial['meal'] = recipe
    context = {}
    
    try:
        meal_plan = Meal_Plan.objects.get(user_id=request.user, is_active = True)
        context.update({'menu_form': menu_form})
        context.update({'meal_plan': meal_plan})

        if request.method == 'POST':
            form = MenuForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('recipe-page')  
    except:
        return redirect('home-page')

    return render(request, 'base/meal_plan.html', context)

@login_required(login_url='login-page')
def deleteMenu(request, pk):
    menu = Menu.objects.get(id=pk)

    if request.method == 'POST':
        menu.delete()
        return redirect('home-page')

    return render(request, 'base/delete.html', {'obj': menu})

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
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
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
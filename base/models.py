from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meal_Time(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Meal_Plan(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Meal(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) 
    energy_kcal = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 

class Day(models.Model):
    meal_plan = models.ForeignKey(Meal_Plan, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date) 

class Menu(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    meal_time = models.ForeignKey(Meal_Time, on_delete=models.SET_NULL, null=True)
    #meals = models.ManyToManyField(Meal, related_name="meals")
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meal_Time(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    energy = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) 
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients', blank=True)
    energy_kcal = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Meal(models.Model):
    meal_time = models.ForeignKey(Meal_Time, on_delete=models.SET_NULL, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)

class Day(models.Model):
    date = models.DateField()
    meal = models.ManyToManyField(Meal)


class Meal_Plan(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    days = models.ManyToManyField(Day, related_name='days')

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



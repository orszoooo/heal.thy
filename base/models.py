from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Meal_Time(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Meal_Plan(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

class Meal(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Meal_Time, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True) 
    description_short = models.TextField(null=True, blank=True)
    meal_picture = models.ImageField(null=True, blank=True, upload_to='images/')
    energy_kcal = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.name 

class Menu(models.Model):
    meal_plan = models.ForeignKey(Meal_Plan, on_delete=models.CASCADE, default=1)
    date = models.DateField(default=timezone.now)
    meal_time = models.ForeignKey(Meal_Time, on_delete=models.SET_NULL, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date','meal_time','created']

    def __str__(self):
        return str(self.date)

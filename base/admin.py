from django.contrib import admin

# Register your models here.
from .models import Meal_Plan, Meal_Time, Meal, Menu

admin.site.register(Meal_Plan)
admin.site.register(Meal_Time)
admin.site.register(Meal)
admin.site.register(Menu)
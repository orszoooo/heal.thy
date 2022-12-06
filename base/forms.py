from django.forms import ModelForm
from .models import Meal, Meal_Plan

class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'
        exclude = ['author']

class MealPlanForm(ModelForm):
    class Meta:
        model = Meal_Plan
        fields = '__all__'
        exclude = ['user_id','is_active']

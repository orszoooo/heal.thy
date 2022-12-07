from django.forms import ModelForm, DateInput
from .models import Meal, Meal_Plan, Menu

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

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        exclude = ['meal_plan']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }
        
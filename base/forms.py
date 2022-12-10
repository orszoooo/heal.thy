from django.forms import ModelForm, DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Meal, Meal_Plan, Menu

class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'
        exclude = ['author','description_short']

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
        
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

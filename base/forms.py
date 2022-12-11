from django.forms import ModelForm, DateInput, Select, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Meal, Meal_Plan, Menu

class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'
        exclude = ['author','description_short']

        widgets = {
            'name': TextInput(attrs={'class':'form-control', 'placeholder':"Put recipe's name here..."}),
            'category': Select(attrs={'class':'form-select', 'placeholder':'Meal Time'}),
            'description': Textarea(attrs={'class':'form-control', 'placeholder':'Put description here...'}),
            'energy_kcal': TextInput(attrs={'class':'form-control', 'placeholder':"Put energy in kcal here..."}),
        }

class MealPlanForm(ModelForm):
    class Meta:
        model = Meal_Plan
        fields = '__all__'
        exclude = ['user_id','is_active']

        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
        }

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        exclude = ['meal_plan']
        widgets = {
            'date': DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'meal_time': Select(attrs={'class':'form-select', 'placeholder':'Meal Time'}),
            'meal': Select(attrs={'class':'form-select', 'placeholder':'Meal'}),
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

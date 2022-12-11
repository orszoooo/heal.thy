from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home-page'),
    path('login/', views.loginPage, name='login-page'),
    path('logout/', views.logoutUser, name='logout-page'),
    path('register/', views.registerPage, name='register-page'),
    path('recipes/', views.recipesPage, name='recipe-page'),
    path('create-meal/', views.createMeal, name='create-meal'),
    path('edit-meal/<str:pk>', views.editMeal, name='edit-meal'),
    path('delete-meal/<str:pk>', views.deleteMeal, name='delete-meal'),
    path('create-plan/', views.createMealPlan, name='create-plan'),
    path('activate-plan/<str:pk>', views.activateMealPlan, name='activate-plan'),
    path('deactivate-plan/<str:pk>', views.deactivateMealPlan, name='deactivate-plan'),
    path('edit-plan/<str:pk>', views.editMealPlan, name='edit-plan'),
    path('delete-plan/<str:pk>', views.deleteMealPlan, name='delete-plan'),
    path('add-menu/<str:pk>', views.addMenu, name='add-menu'),
    path('delete-menu/<str:pk>', views.deleteMenu, name='delete-menu'),
    path('plan-pdf/', views.planPDF, name='plan-pdf'),
    path('profile/',views.profilePage, name="profile-page"),
]

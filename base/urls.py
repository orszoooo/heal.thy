from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home-page'),
    path('login/', views.loginPage, name='login-page'),
    path('logout/', views.logoutUser, name='logout-page'),
    path('register/', views.registerPage, name='register-page'),
]

from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.Home, name='home'),
    # path('login/', views.login, name='login'),
    path('signup/', views.Signup, name='signup'),
    path('profile/', views.Profile, name='profile'),
    path('dashboard/', views.Dashboard, name='dashboard'),
]

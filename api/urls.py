from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.login, name="logout"),
    path('register/', views.login, name="register"),
    path('profile/', views.login, name="profile"),
    path('version/', views.login, name="version"),
]
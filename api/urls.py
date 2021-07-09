from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('profile/', views.profile, name="profile"),
    path('version/', views.version, name="version"),
]
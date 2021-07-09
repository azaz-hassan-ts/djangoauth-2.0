from django.urls import path, include
from django.urls.conf import re_path
from . import views

app_name = 'api'

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('profile/', views.profile, name="profile"),
    re_path('^$', views.version1, name="version1"),
    re_path('^$', views.version2, name="version2"),
]
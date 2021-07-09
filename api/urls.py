from django.urls import path, include
from django.urls.conf import re_path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'api'


schema_view = get_schema_view(
   openapi.Info(
      title="Basic Auth Api",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.basicauth.com/policies/terms/",
      contact=openapi.Contact(email="azaz.hassan@techno.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('profile/', views.profile, name="profile"),
    re_path('^version$', views.version1, name="version1"),
    re_path('^version$', views.version2, name="version2"),
    path(r'', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
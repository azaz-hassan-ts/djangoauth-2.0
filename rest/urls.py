from django.urls import path, include
from django.urls.conf import re_path
from django.contrib import admin




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('api.urls')),
    re_path('^api/',include("api.urls", namespace="v1")),
    re_path('^api/',include("api.urls", namespace="v2"))
]
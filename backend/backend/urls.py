from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/blog/', include('blog.urls')),
    path('api/users/', include('django.contrib.auth.urls')),
    path('api/users/', include('users.urls')),
]

# blog_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from blog.views import MyTokenObtainPairView  # <-- custom view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),  # This gives /api/blogs/
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

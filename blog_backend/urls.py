# blog_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from blog.views import MyTokenObtainPairView  # <-- custom view
from rest_framework_simplejwt.views import TokenRefreshView
from django.http import JsonResponse  # <-- added import

def root_view(request):
    return JsonResponse({"message": "Welcome to the Blog API", "status": "ok"})

urlpatterns = [
    path('', root_view),  # <-- added this line
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),  # This gives /api/blogs/
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

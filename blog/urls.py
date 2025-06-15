# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, RegisterView  # ✅ Import RegisterView

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),  # ✅ Add this line
]

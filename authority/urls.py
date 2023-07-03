from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authority.views import CustomTokenObtainPairView, UserCreateView, UsersView

urlpatterns = [
    path('users/login/', CustomTokenObtainPairView.as_view()),
    path('users/refresh/', TokenRefreshView.as_view()),
    path('users/create/', UserCreateView.as_view()),
    path('users/all/', UsersView.as_view()),
]

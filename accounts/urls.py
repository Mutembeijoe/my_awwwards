from django.urls import path
from .views import UserDetailView, UserCreateView, UserUpdateView

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='update_user'),
    path('register/', UserCreateView.as_view(), name="register" )
]
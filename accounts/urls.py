from django.urls import path
from .views import UserDetailView, UserCreateView

urlpatterns = [
    path('user/<int:pk>', UserDetailView.as_view(), name='profile'),
    path('register/', UserCreateView.as_view(), name="register" )
]
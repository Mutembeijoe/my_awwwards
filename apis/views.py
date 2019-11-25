from django.shortcuts import render
from rest_framework.generics import ListAPIView
from accounts.models import CustomUser
from .serializers import ProfileSerializer

# Create your views here.


class ProfileList(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
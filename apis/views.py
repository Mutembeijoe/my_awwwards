from django.shortcuts import render
from rest_framework.generics import ListAPIView
from accounts.models import CustomUser
from sites.models import Site
from .serializers import ProfileSerializer, SiteSerializer

# Create your views here.


class ProfileList(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer


class SiteList(ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
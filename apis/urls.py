from django.urls import path
from .views import ProfileList, SiteList


urlpatterns = [
    path('profiles/', ProfileList.as_view()),
    path('sites/', SiteList.as_view())
]
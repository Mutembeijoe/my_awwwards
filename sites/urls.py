from django.urls import path
from .views import SiteListView, SiteDetailView, SiteCreateView,SiteUpdateView

urlpatterns = [
    path('', SiteListView.as_view(), name='home'),
    path('site/new/', SiteCreateView.as_view(), name='add_site'),
    path('site/<int:pk>/edit', SiteUpdateView.as_view(), name='edit_site'),
    path('site/<int:pk>', SiteDetailView.as_view(), name='site')
]
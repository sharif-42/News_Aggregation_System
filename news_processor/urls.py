from django.urls import path
from .views import common_views

urlpatterns = [
    path('news-processor/', common_views.Home().as_view(), name='home')
]

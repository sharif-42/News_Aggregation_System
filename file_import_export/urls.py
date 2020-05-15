from django.urls import path, include
from .views import import_export_data

urlpatterns = [
    path('news-processor/', import_export_data)
]

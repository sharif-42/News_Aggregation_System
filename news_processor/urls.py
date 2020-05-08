from django.urls import path,include

from news_processor.views import views

urlpatterns = [
    path('bangla',views.Home.as_view(), name='home')
]
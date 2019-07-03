from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home,name="core-home"),
    path('about/', views.about,name="core-about"),
]
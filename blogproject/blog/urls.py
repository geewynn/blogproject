from django.urls import path, include
from blog import views

urlpatterns = [
    path('index', views.index, name='index'),
]
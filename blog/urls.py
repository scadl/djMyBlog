from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('s_<auk>/', views.section),
    path('p_<auk>/', views.page),
]

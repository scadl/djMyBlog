from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.post_list),
    path('<auk>/', views.post_detail, name='post_detail'),
]

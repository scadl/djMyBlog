from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.post_list),
    path('<auk>/', views.post_detail, name='post_detail'),
]

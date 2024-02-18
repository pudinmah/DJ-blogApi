from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('get-all-posts/',views.GetAllPosts),
    path('create-new-post', views.CreatePost),
]
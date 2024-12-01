# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_all_posts, name='get_all_posts'),
    path('posts/<int:pk>/', views.get_post, name='get_post'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:pk>/update/', views.update_post, name='update_post'),
    path('posts/<int:pk>/delete/', views.delete_post, name='delete_post'),
]

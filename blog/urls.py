from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog-main'),
    path('posts/', views.posts, name='blog-posts'),
    path('posts/<slug:slug>', views.post, name='blog-individual-post')
]

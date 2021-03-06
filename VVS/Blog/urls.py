from django.urls import path
from .import views as blog_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    UserPostListView
)
# followed tutorial: https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3
# for Blog creation html, views and other set up for the Blog
# used to learn jango and how to use html with it
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin 

urlpatterns = [

    path('', PostListView.as_view(), name='Blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),

]






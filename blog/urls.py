from django.urls import path, include

from blog import views

urlpatterns =[
    path('', views.starting_page, name="home"),
    path('posts/', views.posts, name="posts"),
    path('posts/<slug:slug>', views.post_detail, name="post_detail"),
]


from django.urls import path
from . import views

urlpatterns = [
    path("",views.dashboard.as_view(), name='dashboard'),
    path("posts",views.posts.as_view(), name="posts"),
    path("posts/<str:slug>", views.post_details.as_view(), name='post_details') #/posts/my-first-post
]
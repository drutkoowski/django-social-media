from django.urls import path, include
from . import views

urlpatterns = [
    path("create/", views.create_post, name="create_post"),
    path("like/<int:post_id>", views.like_post, name="like_post"),
]
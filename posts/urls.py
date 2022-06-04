from django.urls import path, include
from . import views

urlpatterns = [
    path("create/", views.create_post, name="create_post"),
    path("like/<int:post_id>", views.like_post, name="like_post"),
    path("comment/add/<int:post_id>", views.add_comment, name="add_comment"),
    path("<int:post_id>", views.single_post, name="single_post"),
    path("edit/<int:post_id>", views.edit_post, name="edit_post"),
    path("delete/<int:post_id>", views.delete_post, name="delete_post"),
]
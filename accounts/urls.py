from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("home/", views.home, name="home"),
    path("accounts/edit", views.edit_profile, name="edit_profile"),
    path("accounts/<str:username_slug>", views.profile_page, name="user_profile"),
    path("logout/", views.logout, name="logout"),
    path("unfollow/<int:user_id>", views.unfollow, name="unfollow"),
    path("search/", views.search, name="search"),
    path("home/friends", views.home_friends, name="home_friends"),
    path("stories/create/", views.create_story, name="create_story"),
    path("stories/delete/<int:pk>", views.delete_story, name="delete_story"),
    path("stories/save/<int:pk>", views.save_story, name="save_story"),
    path("stories/category/create", views.create_category, name="create_category"),
    path("stories/category/delete", views.delete_category, name="delete_category"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    path("forgot/password", views.forgot_password, name="forgot_password"),
    path("resetpassword_validate/<uidb64>/<token>/", views.resetpassword_validate, name="resetpassword_validate"),
    path("resetPassword/", views.resetPassword, name="resetPassword"),
]
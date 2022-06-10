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
]
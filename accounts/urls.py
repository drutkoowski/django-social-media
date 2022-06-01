from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("home/", views.home, name="home"),
    path("accounts/<str:username_slug>", views.profile_page, name="user_profile"),
    path("logout/", views.logout, name="logout"),
    path("unfollow/<int:user_id>", views.unfollow, name="unfollow"),
]
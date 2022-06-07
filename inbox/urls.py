from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("/<int:pk>", views.thread, name="thread"),
    path('/create-thread/', views.create_thread, name="create-thread"),
    path('/<int:pk>/create-message/', views.create_message, name="create-message"),

]
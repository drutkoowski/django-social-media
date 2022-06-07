from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("<int:pk>", views.thread, name="thread"),
    path('create-thread/', views.create_thread, name="create-thread"),
    path('create-thread-click/<int:user_pk>/', views.create_thread_click, name="create-thread-click"),
    path('<int:pk>/create-message/', views.create_message, name="create-message"),
    path('notification/<int:notification_pk>/post/<int:post_pk>', views.post_notification, name='post-notification'),
    path('notification/<int:notification_pk>/profile/<str:username_slug>', views.follow_notification,
         name='follow-notification'),
    path('notification/delete/<int:notification_pk>', views.remove_notification, name='notification-delete'),
    path('notification/<int:notification_pk>/thread/<int:object_pk>', views.thread_notification,
         name='thread-notification'),
]
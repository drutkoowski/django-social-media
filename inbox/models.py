from datetime import datetime

from django.db import models


# Create your models here.


class ThreadModel(models.Model):
    user = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE, related_name="+")
    receiver = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)

    def get_last_message(self):
        try:
            get_last_message_of_thread = MessageModel.objects.filter(thread=self).order_by("-date").first()
            last_message = get_last_message_of_thread.body
        except:
            last_message = None
        return last_message

    def get_last_message_owner(self):
        try:
            get_last_message_of_thread = MessageModel.objects.filter(thread=self).order_by("-date").first()
            last_message = get_last_message_of_thread.sender_user
        except:
            last_message = None
        return last_message


class MessageModel(models.Model):
    thread = models.ForeignKey("ThreadModel", related_name="+", on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE, related_name="+")
    receiver_user = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE, related_name="+")
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="uploads/message_photos", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


class Notification(models.Model):
    # 1 = Like, 2 = Comment, 3 = Follow, 4 = DM
    notification_type = models.IntegerField()
    to_user = models.ForeignKey("accounts.UserProfile", related_name='notification_to', on_delete=models.CASCADE,
                                null=True)
    from_user = models.ForeignKey("accounts.UserProfile", related_name='notification_from', on_delete=models.CASCADE,
                                  null=True)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    thread = models.ForeignKey('inbox.ThreadModel', on_delete=models.CASCADE, related_name="+", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    user_has_seen = models.BooleanField(default=False)

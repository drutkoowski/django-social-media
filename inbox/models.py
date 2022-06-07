from django.db import models
from django.utils import timezone

# Create your models here.
from accounts.models import UserProfile


class ThreadModel(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="+")
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="+")

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
    sender_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="+")
    receiver_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="+")
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="uploads/message_photos", blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

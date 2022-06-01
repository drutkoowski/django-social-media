from django.db import models
from accounts.models import UserProfile


# Create your models here.

class UserFollowing(models.Model):
    followed_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followed_by')
    followed_to = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followed_to')
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from accounts.models import Account, UserProfile


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=400, null=True)

import datetime

from django.utils import timezone
from django.db import models
from django_resized import ResizedImageField


class Post(models.Model):
    owner = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=400, null=True)

    def __str__(self):
        return f"{self.pk}"

    def post_likes(self):
        likes = PostLikes.objects.filter(post=self).count()
        return likes

    def post_comments(self):
        comments = PostComments.objects.filter(post=self).count()
        return comments

    def view_recent_comments(self):
        recent_comments = PostComments.objects.filter(post=self).order_by("created_at")[:5].all()
        return recent_comments

    def all_posts_likes(self):
        likes = PostLikes.objects.filter(post=self).all()
        return likes


class PostLikes(models.Model):
    user = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user_id}"

    class Meta:
        verbose_name_plural = "Post Likes"


class PostComments(models.Model):
    user = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content}"

    class Meta:
        verbose_name_plural = "Post Comments"


class Story(models.Model):
    user = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE)
    story_image = ResizedImageField(crop=['middle', 'center'], size=[800, 600], quality=100, blank=True,
                                    upload_to='stories/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_saved = models.BooleanField(default=False)
    expiration_date = models.DateTimeField(default=timezone.now() + datetime.timedelta(days=1))
    category = models.ForeignKey("posts.StoryCategory", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.user.user.username}"

    class Meta:
        verbose_name_plural = "Stories"


class StoryCategory(models.Model):
    user = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE)
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Story Categories"

    def __str__(self):
        return self.category

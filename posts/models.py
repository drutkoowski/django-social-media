from django.db import models


# Create your models here.


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

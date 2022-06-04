from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from followers.models import UserFollowing
from posts.models import Post, PostLikes


# Create your models here.



class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            password=password,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    username_slug = models.SlugField(max_length=50, default="")
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects = MyAccountManager()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username

    def has_perm(self, perm, object=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile', null=True)
    bio = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.user.username

    def followers_count(self):
        followers = UserFollowing.objects.filter(followed_to=self).count()
        return followers

    def following_count(self):
        following = UserFollowing.objects.filter(followed_by=self).count()
        return following

    def posts_count(self):
        posts = Post.objects.filter(owner=self).count()
        return posts

    def get_following_posts(self):
        following_users = UserFollowing.objects.filter(followed_by=self).all()
        user_profiles_list = []
        for user in following_users:
            user_profiles_list.append(user.followed_to.user.username)
        posts_of_followings = Post.objects.filter(owner__user__username__in=user_profiles_list).all()
        return posts_of_followings

    def get_all_liked_posts(self):
        all_liked = PostLikes.objects.filter(user=self).all()
        list_of_id_posts_liked = []
        for like in all_liked:
            list_of_id_posts_liked.append(like.post_id)
        posts_liked = Post.objects.filter(pk__in=list_of_id_posts_liked).all()
        return posts_liked
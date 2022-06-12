import datetime
from itertools import chain
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models import Q

from followers.models import UserFollowing
from inbox.models import ThreadModel
from posts.models import Post, PostLikes, Story, StoryCategory


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

    def get_all_followers(self):
        all_followers_instances = UserFollowing.objects.filter(followed_to=self)
        list_of_id_users = []
        for instance in all_followers_instances:
            list_of_id_users.append(instance.followed_by.pk)
        all_followers_profiles = UserProfile.objects.filter(pk__in=list_of_id_users).all()
        return all_followers_profiles

    def get_all_following(self):
        all_following_instances = UserFollowing.objects.filter(followed_by=self)
        list_of_id_users = []
        for instance in all_following_instances:
            list_of_id_users.append(instance.followed_to.pk)
        all_following_profiles = UserProfile.objects.filter(pk__in=list_of_id_users).all()
        return all_following_profiles

    def dm_suggestions(self):
        dm_suggestions = []
        following_users = UserFollowing.objects.filter(followed_by=self).order_by("-created_at").distinct()[:5]
        for followed in following_users:
            dm_suggestions.append(followed.followed_to)
        all_liked = PostLikes.objects.filter(user=self).values_list('user', flat=True).distinct()[:3]
        random_liked_userprofile_suggestion_query_set = UserProfile.objects.filter(pk__in=all_liked).all()
        for like in random_liked_userprofile_suggestion_query_set:
            dm_suggestions.append(like)
        return dm_suggestions

    def following_suggestions(self):

        list_of_ids = []
        # Get 2 most recent follows by user
        following_users = UserFollowing.objects.filter(followed_by=self).order_by("-created_at").distinct()[:2]
        # Get 2 most recent dm user
        most_recent_dm = ThreadModel.objects.filter(Q(user=self) | Q(receiver=self)).order_by("-created_at").distinct()[
                         :2]
        for x in following_users:
            list_of_ids.append(x.followed_to.pk)
        for x in most_recent_dm:
            if x.user == self:
                list_of_ids.append(x.receiver.pk)
            elif x.receiver == self:
                list_of_ids.append(x.user.pk)
        # list of ids of 2 recent follows and dmed users excluding current user
        final_list_of_ids = []
        for single_id in list_of_ids:
            if not self.pk == single_id:
                if not single_id in final_list_of_ids:
                    final_list_of_ids.append(single_id)

        profile_id_which_user_follows_actually = []
        # All users followed by current user
        following_users = UserFollowing.objects.filter(followed_by=self).order_by("-created_at").distinct().all()
        for x in following_users:
            profile_id_which_user_follows_actually.append(x.followed_to.pk)
        follows_of_user_followings_query = UserFollowing.objects.filter(followed_by__pk__in=final_list_of_ids).order_by(
            "-created_at").distinct()[:4]
        list_of_ids_which_my_followers_follow = []
        for x in follows_of_user_followings_query:
            list_of_ids_which_my_followers_follow.append(x.followed_to.pk)
        ids_to_suggest = []
        for z in list_of_ids_which_my_followers_follow:
            if not z in profile_id_which_user_follows_actually and z != self.pk:
                ids_to_suggest.append(z)

        suggestions = UserProfile.objects.filter(pk__in=ids_to_suggest).all()
        how_many_suggestions_to_fill = 4 - suggestions.count()
        top_followed_users_ids = []
        if how_many_suggestions_to_fill > 1:
            user_profiles = UserProfile.objects.all()
            top_followed_users = sorted(user_profiles, key=lambda ur: (ur.followers_count(), ur.user.date_joined))
            top_followed_users.reverse()
            z = 0
            for x in top_followed_users:
                if z != how_many_suggestions_to_fill and x.pk not in profile_id_which_user_follows_actually and x.pk not in ids_to_suggest and x.pk != self.pk:
                    top_followed_users_ids.append(x.pk)
                    z += 1
            top_followed_users_profiles = UserProfile.objects.filter(pk__in=top_followed_users_ids).all()
            suggestions = chain(suggestions, top_followed_users_profiles)
        return suggestions

    def has_actual_story(self):
        date_from = datetime.datetime.now() - datetime.timedelta(days=1)
        valid_stories = []
        all_user_stories = Story.objects.filter(user=self, created_at__gte=date_from).all()
        for story in all_user_stories:
            if story.expiration_date > datetime.datetime.now():
                valid_stories.append(story)
        has_stories = valid_stories
        if has_stories:
            return True
        else:
            return False

    def user_story_urls(self):
        date_from = datetime.datetime.now() + datetime.timedelta(days=1)
        all_user_stories = Story.objects.filter(user=self, expiration_date__lt=date_from).all()
        return all_user_stories

    def get_saved_stories(self):
        all_saved_user_stories = Story.objects.filter(user=self, is_saved=True).all()
        return all_saved_user_stories

    def get_story_categories(self):
        user_story_categories = StoryCategory.objects.filter(user=self).all()
        return user_story_categories


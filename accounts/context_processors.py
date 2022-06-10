from posts.models import PostLikes
from .models import Account, UserProfile, Post
from django.contrib.auth.models import AnonymousUser


def get_avatar(request):
    if 'admin' in request.path:
        return {}
    if not request.user.is_authenticated or request.user is AnonymousUser:
        return dict(get_avatar=None)
    user = request.user
    userprofile = UserProfile.objects.filter(user=user).first()
    avatar = userprofile.profile_picture.url
    return dict(get_avatar=avatar)


def get_followed_posts(request):
    if 'admin' in request.path:
        return {}
    if not request.user.is_authenticated or request.user is AnonymousUser:
        return dict(followed_posts=None)
    user = request.user
    userprofile = UserProfile.objects.filter(user=user).first()
    followed_posts = userprofile.get_following_posts()
    return dict(get_followed_posts=followed_posts)


def get_liked_posts_by_user(request):
    if 'admin' in request.path:
        return {}
    if not request.user.is_authenticated or request.user is AnonymousUser:
        return dict(get_liked_posts_by_user=None)
    user = request.user
    userprofile = UserProfile.objects.filter(user=user).first()
    all_likes = userprofile.get_all_liked_posts()
    liked_posts_id = []
    for like in all_likes:
        liked_posts_id.append(like.pk)
    all_x = Post.objects.filter(id__in=liked_posts_id).all()
    return dict(get_liked_posts_by_user=all_x)


def get_current_user_profile(request):
    if 'admin' in request.path:
        return {}
    if not request.user.is_authenticated or request.user is AnonymousUser:
        return dict(get_current_user_profile=None)
    user = request.user
    userprofile = UserProfile.objects.filter(user=user).first()
    return dict(get_current_user_profile=userprofile)



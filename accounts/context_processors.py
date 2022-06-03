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
    followed_posts = Post.objects.filter(owner__followed_to=userprofile).all()
    return dict(get_followed_posts=followed_posts)
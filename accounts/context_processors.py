from .models import Account, UserProfile


def get_avatar(request):
    if 'admin' in request.path:
        return {}
    user = request.user
    userprofile = UserProfile.objects.filter(user=user).first()
    avatar = userprofile.profile_picture.url
    return dict(get_avatar=avatar)




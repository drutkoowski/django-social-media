from .models import Account, UserProfile
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




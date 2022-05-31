from django.contrib import admin
from .models import UserFollowing


# Register your models here.
class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ("followed_by", "followed_to")


admin.site.register(UserFollowing, UserFollowingAdmin)

from django.contrib import admin
from .models import UserProfile, Account


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "username", "last_login", "date_joined", "is_active")
    prepopulated_fields = {
        "username_slug": ("username",)
    }
    list_display_links = ("email", "first_name", "last_name")
    readonly_fields = ("last_login", "date_joined")
    ordering = ("-date_joined",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)


#
admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

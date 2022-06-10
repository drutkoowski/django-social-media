from django.contrib import admin
from .models import Post, PostLikes, PostComments, Story


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "description", "created_at")
    ordering = ("-created_at",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class PostLikesAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at")
    ordering = ("-created_at",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class PostCommentsAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content", "created_at")
    ordering = ("-created_at",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class StoryAdmin(admin.ModelAdmin):
    list_display = ("user", "story_image", "is_saved", "expiration_date", "created_at")
    ordering = ("-created_at",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Post, PostAdmin)
admin.site.register(PostLikes, PostLikesAdmin)
admin.site.register(PostComments, PostCommentsAdmin)
admin.site.register(Story, StoryAdmin)

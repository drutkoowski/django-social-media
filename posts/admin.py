from django.contrib import admin
from .models import Post



# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "description", "created_at")
    ordering = ("-created_at",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Post, PostAdmin)

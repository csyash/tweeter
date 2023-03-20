from django.contrib import admin
from .models import CustomUser, Tweet, Comments, Likes, Retweets, UserFollowing
from django.contrib.admin import ModelAdmin

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ["id", "host", "created"]

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name']

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Retweets)
admin.site.register(UserFollowing)

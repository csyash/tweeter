from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    def __str__(self):
        name = self.first_name + ' ' + self.last_name
        if (len(name)==1):
            return self.username
        else:
            return name


class Tweet(models.Model):
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='tweets')
    desciption = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.host.username + ' - ' + self.desciption

class Comments(models.Model):
    commenter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment_description = models.TextField(null=True, blank=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, blank=True, null=True, related_name='comments')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created']
 
    def __str__(self):
        return (self.commenter.username + ' - ' + self.comment_description[0:50])

class Likes(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True, blank=True, related_name='liked')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='liked')

    def __str__(self):
        return (self.user.username + ' liked ' + self.tweet.host.username + " 's tweet")


class Retweets(models.Model):
    Tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='retweets' , null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='retweets', null=True, blank=True)

class UserFollowing(models.Model):
    user_who_is_following = models.ForeignKey(CustomUser, related_name="following", on_delete=models.CASCADE, blank=True, null=True)
    user_who_is_getting_followed = models.ForeignKey(CustomUser, related_name="followers", on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_who_is_following','user_who_is_getting_followed')
        constraints = [
            models.UniqueConstraint(fields=['user_who_is_following','user_who_is_getting_followed'],  name="unique_followers")
        ]

    def __str__(self):
        return self.user_who_is_following.username + ' followed ' + self.user_who_is_getting_followed.username
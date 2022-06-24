from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass

    def __str__(self):
        return f"USER NUMBER '{self.id}' is '{self.username}'. LAST CONNEXION: {self.last_login}."

class Post(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    post = models.TextField(max_length=500)
    datetime = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"POST NUMBER '{self.id}'. BY USER '{self.userid.username}'. CONTENT '{self.post}'. LIKES: '{self.likes}'. PUBLISHED: '{self.datetime}'."

class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_following")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_followed")

    def __str__(self):
        return f"{self.follower.username} (user:{self.follower.id}) FOLLOWS {self.followed.username} (user:{self.followed.id}) "

class Like(models.Model):
    postid = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_id")
    likedby = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_liking")

    def __str__(self):
        return f"USER nº{self.likedby.id} ({self.likedby.username}) LIKES POST nº {self.postid.id} ('{self.postid.post}')"
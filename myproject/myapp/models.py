
from django.db import models
from django.contrib.auth.models import User



class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.word}"

class FBUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)

    full_name = models.CharField(max_length=150)
    bio = models.TextField(blank=True)

    profile_pic = models.ImageField(upload_to='profile/', default='profile/default.png')
    cover_pic = models.ImageField(upload_to='cover/', default='cover/default.png')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
from turtle import title
import django
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dp = models.CharField(max_length=1500)
    intrest = models.TextField()

    def __str__(self) -> str:
        return str(self.username)


class Blog(models.Model):
    bid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    cover = models.CharField(max_length=1500)
    title = models.TextField()
    content = models.TextField()
    date = models.CharField(max_length=20)
    topics = models.TextField()
    count = models.IntegerField()
    duration = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.title)

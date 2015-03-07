from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User)
    article_text = models.TextField()
    article_name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
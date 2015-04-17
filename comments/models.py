from django.db import models
from articles.models import Article
from django.contrib.auth.models import User


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article)
    author = models.ForeignKey(User)
    comment_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blog_article(models.Model):
    title = models.CharField(max_length=100)
    blog_content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete='Protect')
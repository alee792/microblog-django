from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

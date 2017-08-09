from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shop_post_set')
    message = models.TextField()

# Create your models here.

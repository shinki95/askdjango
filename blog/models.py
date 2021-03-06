from django import forms
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
import re

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blgo_post_set')
    title = models.CharField(max_length=100, validators=[min_length_3_validator] )
    content = models.TextField() 
    lnglat = models.CharField(max_length=50, blank=True,
        validators=[lnglat_validator],
        help_text='경도/위도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES )
    tag_set = models.ManyToManyField('Tag', blank=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey('Post')
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
            ordering = ["id"]

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name


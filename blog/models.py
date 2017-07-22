from django import forms
from django.db import models

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    title = models.CharField(max_length=100, validators=[min_length_3_validator] )
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES )
    tag_set = models.ManyToManyField('Tag')


    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]


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


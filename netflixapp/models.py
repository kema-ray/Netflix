from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', related_name='profiles')

AGE_CHOICES = (
    ('All','All'),
    ('Kids','Kids')
)
class Profile(models.Model):
    name = models.CharField(max_length=200)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)

MOVIE_CHOICES=(
    ('seasonal','seasonal'),
    ('single','single')
)
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    category = models.CharField(max_length=10, choices= MOVIE_CHOICES)
    videos = models.ManyToManyField('Video')
    poster = models.ImageField(upload_to='poster')
    age_limit = models.CharField(max_length=10, choices = AGE_CHOICES)

class Video(models.Model):
    title = models.CharField(max_length=200, blank = True, null = True)
    file = models.FileField(upload_to='movies')
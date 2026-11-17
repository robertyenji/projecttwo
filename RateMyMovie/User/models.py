from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Add any additional fields you want for your custom user model
   email = models.EmailField(unique=True)
   bio = models.TextField(blank=True, null=True, max_length=100)
   image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
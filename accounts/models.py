from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=300, blank=True)
    profile_picture = models.ImageField(upload_to=None, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True,)
    linkedin = models.URLField(max_length=100, blank=True)
    x = models.URLField(max_length=70, blank=True)

    def __str__(self):
        return f"{self.username}"
    





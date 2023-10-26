from django.db import models
from accounts.models import CustomUser
from django.utils.text import slugify

# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True, max_length=150)
    content = models.TextField(blank=True)
    author_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ForeignKey(to=Tag, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    author_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    post_id = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=2000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.text 
    









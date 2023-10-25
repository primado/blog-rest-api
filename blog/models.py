from django.db import models
from accounts.models import Authors

# Create your models here.



class Tags(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name
    

class Posts(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    author_id = models.ForeignKey(to=Authors, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ForeignKey(to=Tags, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['-created_at']


class Comments(models.Model):
    author_id = models.ForeignKey(to=Authors, on_delete=models.CASCADE)
    post_id = models.ForeignKey(to=Posts, on_delete=models.CASCADE)
    text = models.CharField(max_length=2000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.text 
    









from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_id', 'display_username', 'title', 'display_blog_status']
    list_select_related = ['author_id', 'id',]

    def display_username(self, request):
        user = request.user.username 
        return user
    
    def display_blog_status(self, obj):
        if obj.is_draft == True:
            return "Draft Mode"
        elif obj.is_published == True:
            return "Published"
        else: None


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_id', 'display_username', 'text',]
    list_select_related = ['text',]


    def display_username(self, request):
        user = request.user.username 
        return user
    

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]


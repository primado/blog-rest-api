from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_id', 'title', 'slug', 'display_blog_status', ]
    list_display_links = ['title', 'slug']
    list_select_related = ['author_id',]

    # def display_username(self, obj):
    #     username = obj.author_id
    #     return username
    
    def display_blog_status(self, obj):
        if obj.is_draft == True:
            return "Draft Mode"
        elif obj.is_published == True:
            return "Published"
        else: None


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_id', 'display_username', 'text',]
    list_select_related = ['author_id',]


    def display_username(self, request):
        user = request.user.username 
        return user
    

@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]


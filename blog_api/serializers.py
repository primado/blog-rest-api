from rest_framework import serializers
from accounts.serializers import CustomUserPostSerializer
from blog.models import *



class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    user = CustomUserPostSerializer()
    tags = TagsSerializer()
    class Meta:
        model = Post
        fields = '__all__'
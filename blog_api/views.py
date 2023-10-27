from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from accounts.models import CustomUser

from rest_framework.permissions import IsAuthenticated
from blog.models import *
from .serializers import *

# Create your views here.


class BlogPostListView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, slug=None):
        try: 
            post = self.queryset.get(slug=slug)
            serializer = self.get_serializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"detail": "Article does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        


        
        


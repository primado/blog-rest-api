from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *


app_name = 'blog_api    '


router = DefaultRouter()
router.register(r'api/blog', BlogPostViewSet)


urlpatterns = [
    path('api/blog/<slug:slug>/', BlogPostViewSet.as_view({'get': 'retrieve'}), name='get-article'),
    path('', include(router.urls)),

]


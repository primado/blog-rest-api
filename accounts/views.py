from django.shortcuts import render
from dj_rest_auth.views import LoginView
from .serializers import CustomLoginSerializer

# Create your views here.


class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer
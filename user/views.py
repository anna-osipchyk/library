from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from user.models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
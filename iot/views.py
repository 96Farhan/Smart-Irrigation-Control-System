"""
Module Name: Views
Descriptipn: Class based and function based views.
"""
from django.contrib.auth.models import User, Group

from .models import Alert

from .serializers import GroupSerializer, UserSerializer, AlertSerializer

from rest_framework import viewsets
from rest_framework.response import Response


class AlertViewSet(viewsets.ModelViewSet):

    queryset = Alert.objects.all().order_by('-timestamp')
    serializer_class = AlertSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

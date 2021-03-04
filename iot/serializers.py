"""
Module Name: serializers
Descriptipn: Serializers allow complex data such as querysets and
             model instances to be converted to native Python datatypes
             that can then be easily rendered into JSON, XML or other
             content types. Serializers also provide deserialization,
             allowing parsed data to be converted back into complex types,
             after first validating the incoming data.
"""
from django.contrib.auth.models import User, Group

from rest_framework import serializers

from .models import Alert


class AlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alert
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

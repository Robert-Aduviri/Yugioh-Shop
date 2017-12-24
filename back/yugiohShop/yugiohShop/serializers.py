from django.contrib.auth.models import User, Group
from rest_framework import serializers
from yugiohShop.models import Carta

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carta
        fields = ('url', 'name')

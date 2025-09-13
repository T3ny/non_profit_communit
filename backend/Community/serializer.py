from rest_framework import serializers
from .models import Group, Event

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'members']

class EventSerializer(serializers.ModelSerializer):
    group_name = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = Event
        fields = ['id', 'group', 'group_name', 'title', 'description', 'date']

from rest_framework import serializers
from .models import User, Flock, Message


class UserSerializer(serializers.ModelSerializer):
    joining_flock = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    managing_flock = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'name', 'about', 'phone', 'status', 'latitude', 'longitude',
            'joining_flock', 'managing_flock'
        ]
        read_only_fields = ['joining_flock', 'managing_flock']


class FlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flock
        fields = [
            'id', 'title', 'description', 'status', 'password',
            'destination', 'latitude', 'longitude',
            'created_at', 'started_at', 'finished_at',
            'leader',
        ]
        # The password is used to gate joining a flock - it must never be
        # readable in API responses (e.g. when listing nearby flocks or
        # fetching flock details), only settable when creating one.
        # It's not `required` here because updates (e.g. starting/finishing
        # a flock) re-send the whole Flock object but the client never has
        # the password after creation; FlockList.post enforces that it's
        # actually provided when a flock is first created.
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
        }


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'created_at', 'user', 'flock']

from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model

User = get_user_model()


class TodoSerializer(serializers.ModelSerializer):

    def validate_priority(self, priority):
        if priority < 1 or priority > 5:
            raise serializers.ValidationError('this is prioritized todo')
        return priority

    class Meta:
        model = Todo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

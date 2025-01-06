from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'created_at', 'completed_at', 'owner']
        read_only_fields = ['id', 'created_at', 'completed_at', 'owner']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['task_url'] = f"/api/tasks/{instance.id}/"
        return representation


from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
    def create(self, validated_data):
        # Create user with hashed password
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        # user = User.objects.create_user(**validated_data)
        # return user


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['task_url'] = f"/api/tasks/{instance.id}/"
        return representation

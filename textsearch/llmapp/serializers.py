from rest_framework import serializers
from llmapp.models import *

class RegisterSerializer(serializers.ModelSerializer):
    conformpassword = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'conformpassword']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['conformpassword']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('conformpassword')  
        user = User.objects.create_user(**validated_data)
        return user

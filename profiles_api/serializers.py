from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    email=serializers.EmailField(max_length=255)

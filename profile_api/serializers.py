from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    ''' Serializer is a name field  for testing our API view'''
    name = serializers.CharField(max_length=20)
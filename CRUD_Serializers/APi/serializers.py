from rest_framework import serializers


class Student_Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    Name = serializers.CharField(max_length=15)
    Roll = serializers.IntegerField()
    City = serializers.CharField(max_length=15)
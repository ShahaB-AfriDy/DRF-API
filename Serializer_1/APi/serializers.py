from rest_framework import serializers



class Student_serializer(serializers.Serializer):
    id = serializers.IntegerField()
    Name = serializers.CharField(max_length=20)
    Roll = serializers.IntegerField()
    Subject = serializers.CharField(max_length=20)
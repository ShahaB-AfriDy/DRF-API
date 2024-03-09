
from APi.models import Student
from rest_framework import serializers

class Student_Serializer(serializers.Serializer):
    Name = serializers.CharField(max_length=20)
    Roll = serializers.IntegerField()
    Subject = serializers.CharField(max_length=20)

    def create(self, validated_data):
        # return super().create(validated_data)
        return Student.objects.create(**validated_data)
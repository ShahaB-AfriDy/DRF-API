from rest_framework import serializers
from api.models import Student

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','Name','Roll','City']
        # fields = "__all__"

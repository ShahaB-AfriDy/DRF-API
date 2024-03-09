from rest_framework import viewsets
from api.models import Student
from api.serializers import Student_Serializer


class Student_View_Model(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer

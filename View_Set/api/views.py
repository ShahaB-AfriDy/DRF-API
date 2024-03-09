from rest_framework.response import Response
from rest_framework import viewsets, status
from api.models import Student
from api.serializers import Student_Serializer


class Student_View(viewsets.ViewSet):
    
    def list(self, request):
        students = Student.objects.all()
        student_serializer = Student_Serializer(students, many=True)
        return Response(student_serializer.data)
    
    def retrieve(self, request, pk=None):
        if pk is not None:
            student = Student.objects.get(pk=pk)
            student_serializer = Student_Serializer(student)
            return Response(student_serializer.data)
    
    def create(self, request):
        student_serializer = Student_Serializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'msg': "Data Saved!"}, status=status.HTTP_201_CREATED)
        return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

        
    def update(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        student_serializer = Student_Serializer(student, data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'msg': "Complete Updated data!"})
        return Response(student_serializer.errors)
    
    def partial_update(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        student_serializer = Student_Serializer(student, data=request.data, partial=True)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'msg': "Partial updated data!"})
        return Response(student_serializer.errors)
    
    def delete(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response({"msg": "Deleted!"}, status=status.HTTP_204_NO_CONTENT)

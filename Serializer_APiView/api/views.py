from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import Student_Serializer
from .models import Student
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Student_List(APIView):
    def get(self,request,id=None,format=None):
        if id is not None:
            students = Student.objects.get(id=id)
            student_serializer = Student_Serializer(students) 
            return Response(student_serializer.data)
        students = Student.objects.all()
        student_serializer = Student_Serializer(students,many=True)
        return Response(student_serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        student_serializer = Student_Serializer(data = request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({"msg":"Data Saved!"},status=status.HTTP_201_CREATED)
        return Response(student_serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        
    def put(self,request,id,format=None):
        student = Student.objects.get(pk=id)
        student_serializer = Student_Serializer(student,data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({"msg":"Completely Updated Data!"})
        return Response(student_serializer.error,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id,format=None):
        student = Student.objects.get(pk=id)
        student_serializer = Student_Serializer(student,data=request.data,partial=True)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({"msg":"Partialy Updated Data!"})
        return Response(student_serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,ruquest,id,format=None):
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({"msg":"deleted!"},status=status.HTTP_404_NOT_FOUND)
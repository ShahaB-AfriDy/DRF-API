from django.shortcuts import render
from APi.serializers import Student_Serializer
from APi.models import Student
from django.http import JsonResponse
# Create your views here.

def Student_List(request):
    if request.method == 'POST':
        return None
    else:
        student = Student.objects.all()
        student_serializer = Student_Serializer(student,many=True)
        return JsonResponse(student_serializer.data,safe=False)





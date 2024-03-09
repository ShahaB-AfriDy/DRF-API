from django.shortcuts import render
from APi.models import Student
from APi.serializers import Student_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse


# Create your views here.

def Student_List(request):
    students = Student.objects.all()
    student_serializer = Student_serializer(students,many=True)
    # json_data = JSONRenderer().render(student_serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(student_serializer.data,safe=False)



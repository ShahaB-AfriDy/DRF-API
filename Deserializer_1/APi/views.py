from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from APi.serializers import Student_Serializer
from django.http import JsonResponse,HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def Student_List(request):
    if request.method == "POST":
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        student_serializer = Student_Serializer(data=python_data)
        if student_serializer.is_valid():
            student_serializer.save()
            # message = {"message":"Data Created!"}
            json_render = JSONRenderer().render({"message":"Data Created!"})
            return HttpResponse(json_render,content_type='application/json')
            return JsonResponse(student_serializer.data)
        
        # json_render = JSONRenderer().render(student_serializer.errors)
        return HttpResponse(json_render,content_type='application/json')
    
    
    
    return HttpResponse("<h1>De-Serialization</h1>")



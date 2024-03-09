from django.shortcuts import render
from api.models import Student
from api.serializers import Student_Serializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# just for get and create the data
class Student_Get_Post(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer

    ## no need the below methods in Concrete View API

    # def get(self,request,*args, **kwargs):
    #     return self.list(request,*args,**kwargs)
    
    # def post(self,request,*args, **kwargs):
    #     return self.create(request,*args,**kwargs)

##  ----------------------------------------------------------------------------
# for update , get_specific instance and delete
class Student_Update_Delete(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer

    ## no need the below methods in Concrete View API

    # def get(self,request,*args, **kwargs):
    #     return self.retrieve(request,*args,**kwargs)
    
    # def put(self,request,*args, **kwargs):
    #     return self.update(request,*args,**kwargs)
    
    # def delete(self,request,*args, **kwargs):
    #     return self.destroy(request,*args,**kwargs)

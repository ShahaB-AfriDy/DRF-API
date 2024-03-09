from django.contrib import admin
from APi.models import Student
# Register your models here.


@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    list_display = ['id','Name','Roll','City']
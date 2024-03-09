from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class Stutent_Admin(admin.ModelAdmin):
    list_display = ['id','Name','Roll',"City"]
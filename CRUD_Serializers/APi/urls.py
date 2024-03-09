from django.urls import path
from APi import views
urlpatterns = [
    path(route='',view=views.Student_List,name='student-list'),
]

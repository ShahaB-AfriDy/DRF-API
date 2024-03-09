from django.urls import path
from APi import views


urlpatterns = [
    path('',views.Student_List,name='Student'),
]

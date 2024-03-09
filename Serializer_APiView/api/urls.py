from django.urls import path
from .views import Student_List


urlpatterns = [
    path('students/',Student_List.as_view(),name='students'),
    path('students/<int:id>/',Student_List.as_view(),name='students'),
]

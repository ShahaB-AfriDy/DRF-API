from django.urls import path
from api.views import Student_Get_Post,Student_Update_Delete

urlpatterns = [
    path('students/',view=Student_Get_Post.as_view(),name='students_get_post'),
    path('students/<int:pk>/',view=Student_Update_Delete.as_view(),name='students_update_delete'),
]

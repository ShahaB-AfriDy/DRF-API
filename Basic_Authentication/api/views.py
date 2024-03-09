from rest_framework import viewsets
from api.models import Student
from api.serializers import Student_Serializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly


class Student_View_Model(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAdminUser]


# user = zeeshan 
# password = khan1234
    
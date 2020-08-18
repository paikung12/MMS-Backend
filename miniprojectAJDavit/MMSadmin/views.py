from django.contrib.auth.models import User
from .serializer import MemberManagementSystemserializers,UserSerializer,CourseManagementSystemserializers
from .models import MemberManagementSystem
from .models import CourseManagementSystem
from rest_framework import viewsets

# Create your views here.
class MemberManagementSystemViewset(viewsets.ModelViewSet):
    queryset = MemberManagementSystem.objects.all()
    serializer_class = MemberManagementSystemserializers

class CourseManagementSystemViewset(viewsets.ModelViewSet):
    queryset = CourseManagementSystem.objects.all()
    serializer_class = CourseManagementSystemserializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
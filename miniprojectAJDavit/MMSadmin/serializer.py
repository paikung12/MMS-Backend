from rest_framework import serializers
from .models import MemberManagementSystem, CourseManagementSystem
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'StudentID']

class CourseManagementSystemserializers(serializers.ModelSerializer):
    class Meta:
        model = CourseManagementSystem
        fields = ['id', 'CourseID', 'NameCourse', 'TeachingPeriod', 'TeacherName', 'CourseStatus', ]

class MemberManagementSystemserializers(serializers.ModelSerializer):
    course_data = CourseManagementSystemserializers(source='course',read_only=True)
    class Meta:
        model = MemberManagementSystem
        fields = ['id', 'course','course_data','StudenID', 'CourseIDEnroll', 'Enrolldate', 'Name', 'Address', 'ContactDetails', 'ParentContac']



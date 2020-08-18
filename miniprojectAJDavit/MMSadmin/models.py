from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class CourseManagementSystem (models.Model):
    CourseID = models.CharField(max_length=20)
    NameCourse = models.CharField(max_length=200)
    TeachingPeriod = models.DateTimeField()
    TeacherName = models.CharField(max_length=200)
    CourseStatus = models.BooleanField()

class MemberManagementSystem(models.Model):
    course = models.ForeignKey(CourseManagementSystem,on_delete=models.CASCADE)
    StudenID = models.CharField(max_length=20,unique=True)
    CourseIDEnroll = models.CharField(max_length=200)
    Enrolldate = models.DateTimeField()
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=250)
    ContactDetails = models.CharField(max_length=200)
    ParentContac = models.CharField(max_length=200)












from django.contrib import admin

# Register your models here.
from MMSadmin.models import MemberManagementSystem,CourseManagementSystem
admin.site.register(MemberManagementSystem)
admin.site.register(CourseManagementSystem)

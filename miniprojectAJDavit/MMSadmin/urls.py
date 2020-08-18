from django.urls import path, include
from rest_framework.routers import DefaultRouter
from MMSadmin import views

router = DefaultRouter()
router.register(r'MemberManagementSystem', views.MemberManagementSystemViewset)
router.register(r'CourseManagementSystem', views.CourseManagementSystemViewset)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
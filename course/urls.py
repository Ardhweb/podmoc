from django.urls import path
from .views import CourseList,CourseDetail
app_name ='course'

urlpatterns=[
        path('list',CourseList.as_view(), name='course_list'),
        path('<int:pk>/course-detials',CourseDetail.as_view(), name='course_details'),
]
from django.urls import path
from .views import CourseList,CourseDetail,enroll_to_course
app_name ='course'

urlpatterns=[
        path('list',CourseList.as_view(), name='course_list'),
        path('<int:pk>/course-detials',CourseDetail.as_view(), name='course_details'),
        path('<int:course_id>/enrollments',enroll_to_course, name='course_enroll'),
]
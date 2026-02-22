from django.urls import path
from .views import CourseList,CourseDetail,enroll_to_course,MyCourseView,complete_lesson
app_name ='course'

urlpatterns=[
        path('list',CourseList.as_view(), name='course_list'),
        path('<int:pk>/course-detials',CourseDetail.as_view(), name='course_details'),
        path('<int:course_id>/enrollments',enroll_to_course, name='course_enroll'),
        path('mycourse',MyCourseView.as_view(), name='course_my'),
         path('complete-lesson/<int:id>/',complete_lesson, name='complete_lesson'),
]
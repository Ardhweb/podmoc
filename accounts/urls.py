from . import views
from django.urls import path
app_name="accounts"

urlpatterns = [
path("students/signup", views.register_student_user,name="student_signup"),
path("students/login", views.login_user, name="student_login"),
path("teacher/signup", views.register_teacher_user, name="teacher_signup"),
path("logout", views.logout_user, name="logout"),
]
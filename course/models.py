from django.db import models

# Create your models here.
from core.models import BaseModel
from accounts.models import User, TeacherProfile, StudentProfile

class Course(BaseModel):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50,null=False,blank=False)
	short_desc = models.TextField(blank=True,max_length=150)
	long_desc = models.TextField(blank=True,max_length=255)

class Lesson(BaseModel):
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
	content = models.TextField(blank=False, max_length=560)
	video_link = models.URLField(blank=True,null=True)
	

class Enrollments(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	student = models.ForeignKey(StudentProfile, on_delete=models.SET_NULL, null=True)
	is_paused = models.BooleanField(default=False)
	grade = models.CharField(max_length=10, null=True, blank=True)
	is_completed = models.BooleanField(default=False)
	progress = models.IntegerField(default=0,blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True) 

	class Meta:
		unique_together = ('course', 'student')


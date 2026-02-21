from django.db import models

# Create your models here.
from core.models import BaseModel
from accounts.models import User

class Course(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,null=False,blank=False)
    short_desc = models.TextField(blank=True,max_length=150)
    long_desc = models.TextField(blank=True,max_length=255)

    def __str__(self):
        return f"{self.title}" or f"No title"

    def get_absolute_url(self):
        return reverse("course-detials", kwargs={"pk": self.pk})

class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=50,null=True,blank=True)
    content = models.TextField(blank=False, max_length=560)
    video_link = models.URLField(blank=True,null=True)

    def __str__(self):
        return f"{self.title}" or f"No title"
    

class Enrollments(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_paused = models.BooleanField(default=False)
    grade = models.CharField(max_length=10, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    progress = models.IntegerField(default=0,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        unique_together = ('course', 'student')

    def get_absolute_url(self):
        return reverse("enrollments", kwargs={"course_id": self.course.pk})


class LessonProgress(models.Model):
    NOT_STARTED = 'not_started'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

    PROGRESS_CHOICES = [
        (NOT_STARTED, 'Not Started Yet'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]
    
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    enrollment = models.ForeignKey(Enrollments, on_delete=models.CASCADE)
    progress = models.CharField(
        max_length=20,
        choices=PROGRESS_CHOICES,
        default=NOT_STARTED,
    )
    completed_at = models.DateTimeField(null=True, blank=True) 

    # class Meta:
    #     unique_together = ('enrollment',) 



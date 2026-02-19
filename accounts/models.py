from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import  UserManager
from django.utils.timezone import now
from datetime import timedelta
from core.models import BaseModel

USER_ROLE_CHOICES = [
    (1, "Teacher"),
    (2, "Students"),
    (3, "Admin staff"),
]
class User(AbstractUser):
    #username = None  # Remove username field
    email = models.EmailField(unique=True)  # Ensure email is unique
    user_role = models.CharField(max_length=50,null=False,blank=False,choices=USER_ROLE_CHOICES)
    is_email_verified = models.BooleanField(default=False)
    #USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Avoid conflict
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Avoid conflict
        blank=True,
    )


class TeacherProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=25,blank=True,null=True)

class StudentProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=25,blank=True,null=True)
  


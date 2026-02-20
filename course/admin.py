from django.contrib import admin

# Register your models here.
from .models import Course,Enrollments, Lesson
from accounts.models import User

class LessonInline(admin.TabularInline):
    model = Lesson
    fields = ['title','content','video_link']
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','created_at', 'updated_at', 'author']
    inlines = [LessonInline]

    

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = User.objects.filter(user_role=User.UserRole.TEACHER)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


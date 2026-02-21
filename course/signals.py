from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Enrollments, LessonProgress

@receiver(post_save, sender=Enrollments)
def create_lesson_progress(sender, instance, created, **kwargs):
    if created:
        # Get all lessons in the course
        lessons = instance.course.lessons.all()
        progress_to_create = [LessonProgress(enrollment=instance,
                lesson=lesson,
                progress='not_started', 
               )
                for lesson in instance.course.lessons.all()
                ]
        LessonProgress.objects.bulk_create(progress_to_create, batch_size=lessons.count())
        
        # # Create a LessonProgress record for each lesson in the course
        # for lesson in lessons:
        #     LessonProgress.objects.create(
        #         enrollment=instance,
        #         lesson=lesson,
        #         progress=0,  # Default progress is 0%
        #         is_completed=False  # Not completed by default
        #     )
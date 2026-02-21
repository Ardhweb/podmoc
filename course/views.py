from django.shortcuts import render

# Create your views here.
from .models import Course,Lesson
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView


class CourseList(ListView):
    model=Course
    context_object_name = "course"
    queryset = Course.objects.all()
    template_name = 'course/list.html'


class CourseDetail(DetailView):
    context_object_name = "course"
    template_name = 'course/details.html'

    def get_object(self,queryset=None):
        return get_object_or_404(Course, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch lessons related to the course
        course_lesson = Lesson.objects.filter(course=self.kwargs['pk']).order_by('-created_at')
        context['course_lesson'] = course_lesson
        return context


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
    #queryset = Course.objects.all()
    template_name = 'course/detail.html'

    def get_queryset(self):
        return get_object_or_404(Course, id=self.kwargs['id'])

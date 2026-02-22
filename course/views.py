from django.shortcuts import render

# Create your views here.
from .models import Course,Lesson,Enrollments,LessonProgress
from django.shortcuts import get_object_or_404,HttpResponse,redirect
from django.views.generic import ListView,DetailView
from .forms import EnrollmentForm
from accounts.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.db.models import FilteredRelation, Q
from django.http import JsonResponse

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
        course_id = self.kwargs['pk']
        user = self.request.user
    
        enrollment = None
        if user.is_authenticated:
            enrollment = Enrollments.objects.filter(
                student=user, 
                course_id=course_id
            ).first()
    
        if enrollment:
            course_lessons = Lesson.objects.filter(course_id=course_id).annotate(
                user_progress=FilteredRelation(
                    'lessonprogress', 
                    condition=Q(lessonprogress__enrollment=enrollment)
                )
            ).select_related('user_progress').order_by('created_at')
        else:
            course_lessons = Lesson.objects.filter(course_id=course_id).order_by('created_at')
    
        context['course_lesson'] = course_lessons
        context['is_enrolled'] = bool(enrollment)
        return context


def enroll_to_course(request,course_id):
    if request.user.is_authenticated and request.method=='POST':
        form = EnrollmentForm(request.POST)
        if request.user.user_role==User.UserRole.STUDENT:
            try:
                if form.is_valid():
                    course = get_object_or_404(Course, id=course_id)
                    enroll = Enrollments.objects.create(student=request.user, course_id=course_id)
                    #lesson_progress = LessonProgress.objects.create_bulk(enrollments=enroll,lesson=)
                    return redirect("course:course_details", pk=course_id)
            except Exception as e:
                return HttpResponse(f"An error occurred: {str(e)}", status=500)
        else:
            return HttpResponse(f"You do not have permission to  enroll please use different account/student account to  enroll:")
    else:
        form = EnrollmentForm()
        course = get_object_or_404(Course, id=course_id)
    return render(request, "course/enroll_page.html", {"form":form,"course":course})


class MyCourseView(LoginRequiredMixin,ListView):
    model = Enrollments
    context_object_name = 'enrolled_courses'
    login_url = '/users/students/login'
    template_name = 'course/my_course.html'

    def get_queryset(self):
        return Enrollments.objects.filter(student=self.request.user).order_by('-created_at')


def complete_lesson(request, id):
    if request.method == "POST":
       # Best for single objects
        progress = LessonProgress.objects.get(id=id)
        progress.progress = "completed"
        progress.save()
        return JsonResponse({'status': 'success'})
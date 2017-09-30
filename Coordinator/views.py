from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
    CreateView,UpdateView,DeleteView)
from django.core.urlresolvers import reverse_lazy

from Students.models import Student
from Coordinator.forms import CoordinatorStudentForm
# Create your views here.
class MatchedStudentsListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'coordinator/student_list.html'
    def get_queryset(self):
        # print(self.request.user.pk)
        # print(self.request.user)
        return Student.objects.exclude(scientist_id__isnull = True)

class UnmatchedStudentsListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'coordinator/student_list.html'
    def get_queryset(self):
        # print(self.request.user.pk)
        # print(self.request.user)
        return Student.objects.exclude(scientist_id__isnull = False)

class MatchStudentsUpdateView(UpdateView):
    model = Student
    context_object_name = "students"
    form_class = CoordinatorStudentForm
    success_url = reverse_lazy('Coordinator:students_list')
    template_name = 'coordinator/student_form.html'

from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
    CreateView,UpdateView,DeleteView)
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from Letters.models import Letter
from teacher.forms import TeacherLettersForm
from registration.models import UserProfileInfo
from Students.models import Student
from . import models

# Create your views here.
class StudentsCreateView(CreateView):
    model = Student
    context_object_name = 'students'
    fields=('scientist','firstname','lastname','grade','stud_class','interest_1','interest_2')
    success_url = reverse_lazy('teacher:students_list')
    def form_valid(self, form):
        obj = form.save(commit=False)
        self.object = obj
        obj.teacher_id = self.request.user.pk
        obj.save()
        return super(StudentsCreateView, self).form_valid(form)

class StudentsListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'Students/student_list.html'
    def get_queryset(self):
        # print(self.request.user.pk)
        # print(self.request.user)
        return Student.objects.filter(teacher_id=self.request.user.pk)
class LettersCreateView(CreateView):
    model = Letter
    context_object_name = 'letters'
    fields=('letterfile','description','student','sent_date','scientist')
    success_url = reverse_lazy('teacher:tletter_list')

    # print(self.kwargs.get('pk'))
    def form_valid(self, form):
        obj = form.save(commit=False)
        self.object = obj
        print(self.request.user)
        obj.user_id = self.request.user.pk
        # obj.letterfile = self.request.FILES['letterfile']
        obj.save()
        # return HttpResponseRedirect(self.get_success_url())
        # form.instance.user_id = self.kwargs.get('pk')
        return super(LettersCreateView, self).form_valid(form)

class LettersListView(ListView):
    model = Letter
    context_object_name = 'letters_list'
    queryset = Letter.objects.order_by('-date_of_upload')
    template_name = 'Letters/tletter_list.html'

    # context_object_name = 'schools' #default is school_list
    # def get_queryset(self):
    #     print(self.request.user)
    #     print(self.request.user.pk)
    #     return Letter.objects.filter(user_id=self.request.user.pk)
class LettersUpdateView(UpdateView):
    model = Letter
    context_object_name = 'letters'
    form_class = TeacherLettersForm
    template_name = "teacher/letter_form.html"
    # fields=('sent_date','letterfile','description','student')
    success_url = reverse_lazy('teacher:tletter_list')

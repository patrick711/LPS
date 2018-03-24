from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
from django_filters import rest_framework as filters
from django.core.urlresolvers import reverse_lazy

from Coordinator.forms import CoordinatorStudentForm,MatchScientist
from Coordinator.tables import StudentTable,SciTable,MatchTable
from registration.models import UserProfileInfo
from Coordinator.filters import StudentListFilter,SciListFilter
from Students.models import Student
from scientist.models import Scientists
from Coordinator.models import Match

# Create your views here.
class DeleteMatch(DeleteView):
    model = Match
    template_name = 'coordinator/del_match.html'
    

class MakeMatch(CreateView):
    model = Match
    context_object_name = "MakeMatch"
    form_class = MatchScientist
    success_url = reverse_lazy('Coordinator:scientists')
    template_name = 'coordinator/student_form.html'

    def get_initial(self):
        return {'scientist':self.kwargs['scientist']}

class FilteredMatches(ExportMixin,SingleTableMixin, FilterView):
    table_class = MatchTable
    model = Match
    template_name = 'coordinator/match_list.html'
    export_name = 'LPS_Matches'
    filter_fields = {'scientist':['exact'],'student':['exact'], 'creationDate':['year','year__gt','year__lt']}
    #filter_fields = ('scientist','student','creationDate')

class FilteredSciListView(ExportMixin,SingleTableMixin, FilterView):
    table_class = SciTable
    model = UserProfileInfo
    template_name = 'coordinator/sci_list.html'
    #filterset_class = SciListFilter
    export_name= 'Scientists'
    filter_fields = {
    'user':['exact'],'user__email':['contains'],'is_matched':['exact']
    }
    #filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
    #     # print(self.request.user.pk)
#         print(self.request.user.email)
         return UserProfileInfo.objects.exclude(is_scientist = False)
    #
    # def get_context_data(self, **kwargs)
    #     data = super().get_context_data(**kwars)

class FilteredStudentListView(ExportMixin,SingleTableMixin, FilterView):
    table_class = StudentTable
    model = Student
    template_name = 'coordinator/stud_list0.html'
    #filterset_class = StudentListFilter
    fields = ['teacher','scientist','firstname','lastname','grade','stud_class']
    filter_fields = {
    'teacher':['exact'],
    'scientist':['exact'],
    'firstname':['contains'],
    'lastname':['contains'],
    'grade':['exact'],
    'stud_class':['exact'],
    }
    export_name= 'Students'

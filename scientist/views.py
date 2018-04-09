from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,
    CreateView,UpdateView,DeleteView)
from django.http import HttpResponseRedirect
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
from django_filters import rest_framework as filters

from scientist.forms import ScientistMailingAddressForm,ScientistLettersForm,ScientistMatchRequestForm
from scientist.models import ScientistMailingAddress,Scientists, MatchRequest
from registration.models import UserProfileInfo
from Students.models import Student
from Letters.models import Letter
from scientist.tables import MatchRequestTable

# Create your views here.
class ScientistRequestMatchCreateView(CreateView):
    model = MatchRequest
    #fields=('startingDate',)
    success_url = reverse_lazy('scientist:Requests')
    form_class = ScientistMatchRequestForm
    def form_valid(self,form):
        obj = form.save(commit=False)
        self.object = obj
        obj.scientist = UserProfileInfo.objects.get(user=self.request.user)
        obj.isPending = True
        obj.save()
        return super(ScientistRequestMatchCreateView,self).form_valid(form)

class ScientistMatchRequestListView(ExportMixin,SingleTableMixin, FilterView):
    table_class = MatchRequestTable
    model = MatchRequest
    template_name = 'scientist/matchrequest_list.html'
    export_name = 'requests'
    filter_fields = {'scientist':['exact'],'isPending':['exact'], 'startingDate':['year','year__gt','year__lt']}
    #filter_fields = ('scientist','student','creationDate')
    # def get_queryset(self):
    #     return MatchRequest.objects.filter(scientist=self.request.user.id)
    def get_queryset(self):
        print (self.request.user.id)
        return MatchRequest.objects.filter(scientist=UserProfileInfo.objects.get(user=self.request.user))

class ScientistMailingAddressCreateView(CreateView):
    model = ScientistMailingAddress
    fields=('address_1','address_2','city','state','zip_code')
    success_url = reverse_lazy('scientist:list')
    # print(self.kwargs.get('pk'))
    def form_valid(self, form):
        obj = form.save(commit=False)
        self.object = obj
        print(self.request.user)
        obj.user_id = self.request.user.pk
        obj.save()
        # return HttpResponseRedirect(self.get_success_url())
        # form.instance.user_id = self.kwargs.get('pk')
        return super(ScientistMailingAddressCreateView, self).form_valid(form)

class ScientistMailingAddressUpdateView(UpdateView):
    model = ScientistMailingAddress
    fields=('address_1','address_2','city','state','zip_code')
    success_url = reverse_lazy('scientist:list')

class ScientistMailingAddressListView(ListView):
    model = ScientistMailingAddress
    context_object_name = 'scimailingaddresses'
    # context_object_name = 'schools' #default is school_list
    def get_queryset(self):
        return ScientistMailingAddress.objects.filter(user_id=self.request.user.pk)

class ScientistMailingAddressDeleteView(DeleteView):
    model = ScientistMailingAddress
    success_url = reverse_lazy('scientist:list')

class ScientistMailingAddressListView(ListView):
    model = ScientistMailingAddress
    context_object_name = 'scimailingaddresses'
    # context_object_name = 'schools' #default is school_list
    def get_queryset(self):
        return ScientistMailingAddress.objects.filter(user_id=self.request.user.pk)


class LettersCreateView(CreateView):
    model = Letter
    context_object_name = 'letters'
    # fields=('letterfile',)
    success_url = reverse_lazy('scientist:letter_list')
    form_class = ScientistLettersForm
    # print(self.kwargs.get('pk'))
    def form_valid(self, form):
        obj = form.save(commit=False)
        self.object = obj
        # print(self.request.user)
        obj.scientist_id = self.request.user.pk
        obj.from_scientist = True
        obj.save()
        return super(LettersCreateView, self).form_valid(form)

class LettersListView(ListView):
    model = Letter
    context_object_name = 'letters_list'
    queryset = Student.objects.order_by('-date_of_upload')
    # context_object_name = 'schools' #default is school_list
    def get_queryset(self):
        # print(self.request.user.pk)
        # print(self.request.user)
        return Letter.objects.filter(scientist_id=self.request.user.pk)

class LettersUpdateView(UpdateView):
    model = Letter
    context_object_name = 'letters'
    form_class = ScientistLettersForm
    template_name = "scientist/scientistletters_form.html"
    # fields=('sent_date','letterfile','description','student')
    success_url = reverse_lazy('scientist:letter_list')
    def form_valid(self, form):
        obj = form.save(commit=False)
        self.object = obj
        obj.from_scientist = True
        obj.save()
        return super(LettersCreateView, self).form_valid(form)

class StudentsListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'scientist/student_list.html'
    def get_queryset(self):
        # print(self.request.user.pk)
        # print(self.request.user)
        return Student.objects.filter(scientist_id=self.request.user.pk)

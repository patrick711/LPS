import django_tables2 as tables
from django_tables2.utils import A
from Students.models import Student
from registration.models import UserProfileInfo
from Coordinator.models import Match

class MatchTable(tables.Table):
    deleteMatch = tables.LinkColumn('Coordinator:DeleteMatch',args=[A('pk')],text='Delete')
    class Meta:
        model = Match
        attrs = {"class": "table table-striped table-bordered table-lg table-hover"}
        template_name = 'django_tables2/bootstrap.html'
        fields = ['scientist','student','is_active','creationDate','ActiveDate','DeactiveDate','deleteMatch']

class SciTable(tables.Table):
    user = tables.LinkColumn('Coordinator:MakeMatch',args=[A('pk')],
                            verbose_name='User (click to match)')
    is_being_matched = tables.Column(verbose_name='Requesting Match')
    class Meta:
        model = UserProfileInfo
        attrs = {"class": "table table-striped table-bordered table-lg table-hover"}
        template_name = 'django_tables2/bootstrap.html'
        fields = ['user','user.email','is_being_matched','is_matched']

class TeachTable(tables.Table):

    class Meta:
        model = UserProfileInfo
        attrs = {"class": "table table-striped table-bordered table-lg table-hover"}
        template_name = 'django_tables2/bootstrap.html'
        fields = ['user','user.email',]


class StudentTable(tables.Table):

  class Meta:
    model = Student
    fields = ['teacher','scientist','firstname','lastname','grade',
        'stud_class','interest_1','interest_2','date_of_upload']
    attrs = {"class": "table table-striped table-bordered table-lg table-hover"}
    template_name = 'django_tables2/bootstrap.html'
    empty_text = "There are no customers matching the search criteria..."
    export_formats = ['csv','xls','xlsx']

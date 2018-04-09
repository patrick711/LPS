import django_tables2 as tables
from django_tables2.utils import A
from Students.models import Student
from registration.models import UserProfileInfo
from Coordinator.models import Match
from scientist.models import MatchRequest

class MatchRequestTable(tables.Table):
    class Meta:
        model = MatchRequest
        attrs = {"class": "table table-striped table-bordered table-lg table-hover"}
        template_name = 'django_tables2/bootstrap.html'
        fields = ['scientist','creationDate','isPending','startingDate',]

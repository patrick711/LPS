import django_filters
from Students.models import Student
from registration.models import UserProfileInfo
from .tables import SciTable

class StudentListFilter(django_filters.FilterSet):

    class Meta:
        model = Student
        fields = ['teacher','scientist','firstname','lastname','grade','stud_class']
        #order_by = ['pk']

class SciListFilter(django_filters.FilterSet):

    class Meta:
        table_class = SciTable
        model = UserProfileInfo
        fields = ['user__email','is_matched']
        
        #order_by = ['pk']

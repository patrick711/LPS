from django import forms
from Students.models import Student

class CoordinatorStudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('scientist',)
        labels = {
        'scientist':"Scientist",
        }

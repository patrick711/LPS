#from crispy_forms.helper import FormHelper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineField, FormActions,StrictButton
from django import forms

from Students.models import Student
from scientist.models import Scientists
from registration.models import UserProfileInfo
from Coordinator.models import Match

class MatchScientist(forms.ModelForm):
    class Meta():
        model = Match
        
        fields = ('scientist','student','is_active')
        labels = { 'scientist':"Scientist",
                    'student':'Student',
                    'is_active':'Active Match?',
        }
class CoordinatorStudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('scientist',)
        labels = {
        'scientist':"Scientist",
        }


class StudentListFormHelper(FormHelper):
    form_id = 'student-search-form'
    form_class = 'form-inline'
    field_template = 'bootstrap3/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    layout = Layout(
                Fieldset(
                    '<i class="fa fa-search"></i> Search Student Records',
                    InlineField('teacher'),
                    InlineField('student_last_name'),
                    InlineField('student_first_name'),
                    InlineField('primary_phone'),
                ),
                FormActions(
                    StrictButton(
                        '<i class="fa fa-search"></i> Search',
                        type='submit',
                        css_class='btn-primary',
                        style='margin-top:10px;')
                )
    )

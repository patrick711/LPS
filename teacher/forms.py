from django import forms
from Letters.models import Letter

class TeacherLettersForm(forms.ModelForm):
    class Meta():
        model = Letter
        fields = ('received_date',)
        labels = {
        'received_date':"Received Date",
        }

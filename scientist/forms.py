from django import forms
from django.core import validators
from registration.models import UserProfileInfo
from django.contrib.auth.models import User
from scientist.models import ScientistMailingAddress, MatchRequest
from Letters.models import Letter
#def check_for_z(value):
#    if value[0].upper() != 'Z':
#        raise forms.ValidationError("Name needs to start with Z!!")

class DateInput(forms.DateInput):
    input_type = 'date'

class ScientistMatchRequestForm(forms.ModelForm):

    class Meta():
        model = MatchRequest
        fields = ('startingDate',)
        labels = {
        'startingDate': "Start Date",

        }
        widgets = {'startingDate':DateInput(),}



class ScientistMailingAddressForm(forms.ModelForm):

    class Meta():
        model = ScientistMailingAddress
        fields = ('address_1','address_2','city','state','zip_code')
        labels = {
        'zip_code': "Zip Code",
        'address_1':"Address",
        'address_2':"Address cont"
        }

class ScientistLettersForm(forms.ModelForm):
    class Meta():
        model = Letter
        fields = ('letterfile','description','student','sent_date',)
        labels = {
        'letterfile':"Letter",
        'description':"Description",
        'student':"For Student",
        'sent_date':"Date Sent"
        }
        widgets = {'sent_date':DateInput(),}

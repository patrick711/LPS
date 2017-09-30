from django import forms
from django.core import validators
from registration.models import UserProfileInfo
from django.contrib.auth.models import User
#def check_for_z(value):
#    if value[0].upper() != 'Z':
#        raise forms.ValidationError("Name needs to start with Z!!")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('is_scientist','is_coordinator','is_teacher')
        labels = {
        "is_scientist": "I am a Scientist",
        "is_coordinator": "I am a Coordinator",
        "is_teacher": "I am a Teacher!"
        }

class FormName(forms.Form):
    #name= forms.CharField(validators=[check_for_z])
    name= forms.CharField()
    email = forms.EmailField()
    verifyemail = forms.EmailField(label='Re-enter email')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verifyemail']
        if email != vmail:
            raise forms.ValidationError("emails don't match sucka!")
    #def clean_botcatcher(self):
    #    botcatcher = self.cleaned_data['botcatcher']
    #    if len(botcatcher)>0:
    #        raise forms.ValidationError("Gotcha Bot!")
    #        return botcatcher

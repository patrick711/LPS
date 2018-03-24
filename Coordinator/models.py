from django.db import models

from registration.models import UserProfileInfo
from Students.models import Student
# Create your models here.
class Match(models.Model):
    scientist = models.ForeignKey(UserProfileInfo,related_name='Assigned_scientist',blank=True,null=True,limit_choices_to={'is_scientist':True})
    student = models.ForeignKey(Student,related_name='Assigned_student',blank=True,null=True)
    creationDate = models.DateField(auto_now_add=True)
    ActiveDate = models.DateField(auto_now_add=False,null=True)
    DeactiveDate  = models.DateField(auto_now_add=False,null=True)
    is_active = models.BooleanField(default=False)

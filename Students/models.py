from django.db import models
from django.contrib.auth.models import User
from registration.models import UserProfileInfo

# Create your models here.
class Student(models.Model):
    teacher = models.ForeignKey(User,related_name='Teacher')
    scientist = models.ForeignKey(User,related_name='Assigned_scientist',blank=True,null=True)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=50)
    grade = models.IntegerField()
    stud_class = models.CharField(max_length=50)
    interest_1 = models.CharField(max_length=128)
    interest_2 = models.CharField(max_length=128)
    date_of_upload = models.DateField(auto_now_add=True)
    def __str__(self):
    # Built-in attribute of django.contrib.auth.models.User !
        return self.firstname +"_"+ self.lastname

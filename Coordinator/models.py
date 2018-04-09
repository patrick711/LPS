from django.db import models
import csv
from django.contrib.auth.models import User

from registration.models import UserProfileInfo
from Students.models import Student
from teacher.models import Teachers
# Create your models here.
class Match(models.Model):
    scientist = models.ForeignKey(UserProfileInfo,related_name='Assigned_scientist',blank=True,null=True,limit_choices_to={'is_scientist':True})
    student = models.ForeignKey(Student,related_name='Assigned_student',blank=True,null=True)
    creationDate = models.DateField(auto_now_add=True)
    ActiveDate = models.DateField(auto_now_add=False,null=True)
    DeactiveDate  = models.DateField(auto_now_add=False,null=True)
    is_active = models.BooleanField(default=False)

class CSVFile(models.Model):
    csv_file = models.FileField(upload_to='csvfiles')
    creationDate = models.DateField(auto_now_add=True)

    def save(self,*args,**kwargs):
        super(CSVFile,self).save(*args,**kwargs)
        self.csv_file.open(mode='r')
        f = csv.reader(self.csv_file)
        for row in f:

            row_dict = self.row_to_dict(row)
            if row_dict['Teacher'] == 'Teacher':
                continue
            teacher = self.retrieve_teacher(row_dict['Teacher'])
            if teacher:
                print(row_dict)
                student = self.does_stud_exist(row_dict['Firstname'],row_dict['Lastname'],row_dict['Grade'])
                if student is None:
                    print(row_dict)
                    self.create_student(teacher,row_dict)

        self.csv_file.close()

    def retrieve_teacher(self,teacher):
        try:
            return User.objects.get(username=teacher)

        except User.DoesNotExist:
            return None

    def does_stud_exist(self,firstname,lastname,grade):

        try:
            return Student.objects.get(firstname=firstname,lastname=lastname,grade=grade)
        except Student.DoesNotExist:
            return None
        except Student.MultipleObjectsReturned:
            return Student.objects.filter(firstname=firstname,lastname=lastname,grade=grade)[0]

    def row_to_dict(self,row):
        return {'Teacher':row[0],'Scientist':row[1],'Firstname':row[2],'Lastname':row[3],'Grade':row[4],'Stud Class':row[5],
        'Interest 1':row[6],'Interest 2':row[7]}

    def create_student(self,teacher,row_dict):
        Student.objects.create(
            teacher = teacher,
            firstname = row_dict['Firstname'],
            lastname = row_dict['Lastname'],
            grade = row_dict['Grade'],
            stud_class = row_dict['Stud Class'],
            interest_1 = row_dict['Interest 1'],
            interest_2 = row_dict['Interest 2'],
        )

from django.db import models
from django.contrib.auth.models import User
from registration.models import UserProfileInfo
from Students.models import Student
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'letters/user_{0}/{1}'.format(instance.scientist, filename)


class Letter(models.Model):
    letterfile = models.FileField(upload_to='letters/',blank=True)
    date_of_upload = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=100,default=' ')
    scientist = models.ForeignKey(User,related_name='Scientist')
    student = models.ForeignKey(Student)
    sent_date = models.DateField(blank=True,null=True)
    received_date = models.DateField(blank=True,null=True)
    from_student = models.BooleanField(default=False)
    from_scientist = models.BooleanField(default=False)
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.description

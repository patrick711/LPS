from django.db import models
from django.contrib.auth.models import User
from django_localflavor_us.models import USStateField
from registration.models import UserProfileInfo
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'letters/user_{0}/{1}'.format(instance.user, filename)

class TeacherLetters(models.Model):
    user = models.ForeignKey(User)
    letterfile = models.FileField(upload_to=user_directory_path,blank=True)
    date_of_upload = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=100,default=' ')
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

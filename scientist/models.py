from django.db import models
from django.contrib.auth.models import User
from django_localflavor_us.models import USStateField
from registration.models import UserProfileInfo
from Letters.models import Letter
from Students.models import Student

# Create your models here.
class ScientistMailingAddress(models.Model):
    user = models.OneToOneField(User)
    #user = models.OneToOneField(User)
    address_1 = models.CharField( max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField( max_length=64)
    state = USStateField()
    zip_code = models.CharField( max_length=5)

    def get_absolute_url(self):
        return reverse("scientist:updateaddress",kwargs={'pk':self.pk})
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

class Scientists(models.Model):
    user=models.OneToOneField(User)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'letters/user_{0}/{1}'.format(instance.user, filename)

class MatchRequest(models.Model):
    scientist = models.ForeignKey(UserProfileInfo,related_name='Requesting_scientist',blank=True,null=True,
        limit_choices_to={'is_scientist':True})
    creationDate = models.DateField(auto_now_add=True)
    fulfilledDate = models.DateField(auto_now_add=False,null=True)
    student = models.ForeignKey(Student,related_name='Matched_student',blank=True,null=True)
    isPending = models.BooleanField(default=True)
    startingDate = models.DateField(auto_now_add=False,null=True)
    def __str__(self):
        return self.scientist.user.username



# class ScientistLetters(models.Model):
#     user = models.ForeignKey(User)
#     letter = models.ForeignKey(Letter)
#     # letterfile = models.FileField(upload_to=user_directory_path,blank=True)
#     # date_of_upload = models.DateField(auto_now_add=True)
#     # description = models.CharField(max_length=100,default=' ')
#     def __str__(self):
#         # Built-in attribute of django.contrib.auth.models.User !
#         return self.letter.description

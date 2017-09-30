from django.db import models
from django.contrib.auth.models import User
from django_localflavor_us.models import USStateField
from registration.models import UserProfileInfo
from Letters.models import Letter

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

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'letters/user_{0}/{1}'.format(instance.user, filename)

# class ScientistLetters(models.Model):
#     user = models.ForeignKey(User)
#     letter = models.ForeignKey(Letter)
#     # letterfile = models.FileField(upload_to=user_directory_path,blank=True)
#     # date_of_upload = models.DateField(auto_now_add=True)
#     # description = models.CharField(max_length=100,default=' ')
#     def __str__(self):
#         # Built-in attribute of django.contrib.auth.models.User !
#         return self.letter.description

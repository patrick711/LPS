from django.db import models
from django.contrib.auth.models import User
# from django_localflavor_us.models import USStateField

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)
    # Add any additional attributes you want
    # portfolio_site = models.URLField(blank=True)
    is_scientist = models.BooleanField(default=False)
    is_coordinator = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_matched = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_being_matched = models.BooleanField(default=False)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

    # def __init__(self, *args, **kwargs):
    #     super(UserProfileInfo, self).__init__(*args, **kwargs)
    #     self.fields['portfolio_site'].widget.attrs.update({'class' : 'form-control'})

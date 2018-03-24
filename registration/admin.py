from django.contrib import admin
from registration.models import UserProfileInfo, User

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user','is_scientist','is_coordinator','is_teacher','is_matched','is_active','is_being_matched')
    list_display_links = ('pk',)

admin.site.register(UserProfileInfo,UserProfileAdmin)

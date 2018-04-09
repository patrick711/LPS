from django.contrib import admin
from scientist.models import ScientistMailingAddress,MatchRequest,Scientists
# Register your models here.
admin.site.register(ScientistMailingAddress)
admin.site.register(MatchRequest)

# admin.site.register(ScientistLetters)
# admin.site.register(ScientistStudentInfo)

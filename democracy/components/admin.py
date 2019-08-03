from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(SystemUser)
admin.site.register(Poll)
admin.site.register(Candidate)
admin.site.register(Poll_Candidate)
admin.site.register(Vote)
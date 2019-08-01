from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SystemUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    type_choices = [('M', 'MANAGER'),('R','REGULAR')]        
    user_type = models.CharField(max_length=10, choices=type_choices)

    def __str__(self):
        return self.user.username
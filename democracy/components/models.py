from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SystemUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    type_choices = [('M', 'MANAGER'),('R','REGULAR')]        
    user_type = models.CharField(max_length=10, choices=type_choices)

    def __str__(self):
        return self.user.username

class Poll(models.Model):
    owner = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    


class Candidate(models.Model):
    owner = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'pic_folder/')

    def __str__(self):
        return self.name
    
class Poll_Candidate(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.poll.title + " and " +self.candidate.name
    
class Vote(models.Model):
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.poll.title + " and " +self.candidate.name + " and "+self.user.user.username
    
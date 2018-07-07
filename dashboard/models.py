from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager

# Test model
class Note(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name + 'by' + user

class Account(models.Model):
    nickname = models.CharField(max_length=24, blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    birthdate = models.DateField()
    def __str__(self):
        return 'Name: ' + user

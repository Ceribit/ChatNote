from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    first_name = models.CharField(max_length = 24,
                                help_text='Optional.')
    last_name = models.CharField(max_length = 24,
                                help_text='Optional.')
    email = models.EmailField(max_length = 254)
    birth_date = models.DateField(null=True, blank = True)

    def __str__(self):
        return (self.user.username + ":" + self.last_name
                + ',' + self.first_name)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender,instance, **kwargs):
    instance.profile.save()

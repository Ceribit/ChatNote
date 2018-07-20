from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

NOTIFICATION_TEXT = 1
NOTIFICATION_FRIEND_REQUEST = 2
NOTIFICATION_TYPES = (
    (NOTIFICATION_TEXT, 'TEXT'),
    (NOTIFICATION_FRIEND_REQUEST, 'FRIEND_REQUEST'),
)

""" Notification Model """
class Notification(models.Model):
    from_user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.CharField(max_length = 120)
    type = models.IntegerField(choices = NOTIFICATION_TYPES)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return ("Friend request to " + self.from_user)


""" Friend Model """
class Friend(models.Model):
    target_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.target_user.username


""" User Profile Model """
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    first_name = models.CharField(max_length = 24,
                                help_text='Optional.')
    last_name = models.CharField(max_length = 24,
                                help_text='Optional.')
    email = models.EmailField(max_length = 254)
    birth_date = models.DateField(null=True, blank = True)
    friends = models.ManyToManyField(Friend)
    notifications = models.ForeignKey(Notification, on_delete=models.CASCADE)

    #Notification Methods
    def send_friend_request(self, target_user, message, type):
        if self.friends.filter(target_user=target_user).exists():
            target_user.profile.notifications.create(
            from_user = self,
            message = message,
            type = type
            )
            return True
        else:
            return False

    def accept_friend_request(self, target_user):
        request = self.notifications.filter(from_user = target_user,
                                     type = NOTIFICATION_FRIEND_REQUEST)
        if request.exists():
            self.add_friend(target_user)
            request.get().delete()

    # Friend Methods
    def get_friends(self):
        friends_list = self.friends.all()
        users_list = []
        for person in friends_list:
            users_list.append(person.target_user)
        return users_list

    def add_friend(self, target_user): #possible bug
        if not self.user == target_user:
            if not self.friends.filter(target_user=target_user).exists():
                self.friends.create(target_user=target_user)
                target_user.profile.friends.create(target_user=self.user)
                return True
            else:
                if self.friends.filter(target_user = target_user).exists():
                    print("Friendship found from " + self.user)
                if target_user.profile.friends.filter(target_user = self.user).exists():
                    print("Friendship found from " + target_user)
                return False
        return False

    def remove_friend(self, target_user):
        if self.friends.filter(target_user=User.objects.get(username=target_user)).exists():
            oldfriend = self.friends.get(target_user=User.objects.get(username=target_user))
        else: oldfriend = 0
        if oldfriend:
            ex_friend = oldfriend
            ex_friend.delete()
            #stranger = User.objects.get(username=target_user)
            #stranger.profile.friends.filter(target_user=self.username).delete()
            return True
        else:
            return False

    # Class Methods
    def __str__(self):
        return (self.user.username + ":" + self.last_name
                + ',' + self.first_name)





""" Create Accounts """
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender,instance, **kwargs):
    instance.profile.save()

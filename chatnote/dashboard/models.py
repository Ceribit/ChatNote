from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
# Tags and Note model
class Tag(models.Model):
    word = models.CharField(max_length = 25)
    def __str__(self):
        return self.word
    def __unicode__(self):
        return self.word
    def __repr__(self):
        return self.word


class Note(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    tags = models.ManyToManyField(Tag)
    tags_list = ""

    PUBLIC = "PUBLIC"
    FRIENDS_ONLY = "FRIEND"
    GROUP = "GROUP"
    PRIVATE = "PRIVATE"
    PRIVACY_CHOICES = (
        (PRIVATE, 1),
        (FRIENDS_ONLY, 2),
        (PUBLIC, 3),
        (GROUP, 4),

    )
    privacy = models.CharField(max_length = 7,
            choices = PRIVACY_CHOICES, default=PRIVATE)

    def loadTagsList(self):
        self.tags_list = ",".join(str(tag) for tag in self.tags.all())
        return 1
    def __str__(self):
        return self.description

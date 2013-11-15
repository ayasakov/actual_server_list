from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    login_nova = models.CharField(max_length=30, blank=True)
    password_nova = models.CharField(max_length=30, blank=True)
    project_id = models.CharField(max_length=30, blank=True)
    auth_url = models.CharField(max_length=30, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

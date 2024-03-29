from django.db import models

from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional attributes we want to specify in the registration form

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='basic_app/profile_pics' ,blank=True)

    def __str__(self):

        return self.user.username


# Create your models here.

# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(
        verbose_name=u'Телефон',
        max_length=12
    )


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
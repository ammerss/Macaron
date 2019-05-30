from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True,on_delete=models.CASCADE)
    name = models.TextField(max_length=20)
    user_type = models.BooleanField ( default=False, help_text = 'Flag if user is owner = true',null=True )
    phone = models.TextField(max_length=11)
    email = models.EmailField(max_length=254,blank=True,null=True)
    # phone = PhoneNumberField(null=False, blank=False, unique=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
    user_type = models.CharField(max_length=1, null=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
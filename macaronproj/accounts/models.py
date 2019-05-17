from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
    phone = PhoneNumberField(null=False, blank=False, unique=True)
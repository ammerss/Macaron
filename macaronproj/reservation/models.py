from django.db import models

class Resevation(models.Model):
    reser_num = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=128)
    macaron_name = models.CharField(max_length=128)
    macaron_num = models.IntegerField(primary_key=True)
    macaron_price = models.IntegerField(primary_key=True)
    reser_date = models.DateTimeField('date published')
    reser_time = models.DateTimeField('date published')

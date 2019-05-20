from django.db import models

class Resevation(models.Model):
    reser_num = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=128)
    shop_name = models.CharField(max_length=128)
    macaron_name = models.CharField(max_length=128)
    macaron_num = models.IntegerField()
    macaron_price = models.IntegerField()
    reser_request_time = models.DateTimeField() #예약 요청 한 시각
    reser_time = models.DateTimeField(auto_now_add = True) #예약 날짜//픽업날짜

def __str__(self):
        return self.reser_num
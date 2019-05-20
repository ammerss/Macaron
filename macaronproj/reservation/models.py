from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser

class Resevation(models.Model):
    reser_num = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    #shop_name = models.ForeignKey(Store, on_delete=models.CASCADE )
    #choice_macaron = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)
    amount = models.IntegerField(default = 0) #결제금액
    reser_request_time = models.DateTimeField() #예약 요청 한 시각
    reser_time = models.DateTimeField(auto_now_add = True) #예약 날짜//픽업날짜

def __str__(self):
        return self.reser_num
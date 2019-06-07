from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from store.models import Store

class Reservation(models.Model):
    reser_num = models.CharField(primary_key=True,max_length=20, default='')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_name = models.ForeignKey(Store, on_delete=models.CASCADE, default=0 )
    choice_macaron = models.CharField(max_length=10, default='')
    quantity = models.IntegerField(default = 0)
    amount = models.IntegerField(default = 0) #결제금액
    reser_request_time = models.DateTimeField(auto_now_add = True) #예약 요청 한 시각
    reser_time = models.DateTimeField() #예약 날짜//픽업날짜
    approve = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.reser_num)
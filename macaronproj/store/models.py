from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Store(models.Model):
    objects=models.Manager()
    name=models.CharField(max_length=20,blank=False)
    num=models.CharField(max_length=20,blank=False)
    content = models.TextField(blank=False)
    store_pic = models.ImageField(blank=False, upload_to="images/%Y/%m/%d")
    owner=models.ForeignKey(User,editable=False,on_delete=models.CASCADE,default='1')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('store:detail',args=[str(self.pk)])


class Macarons(models.Model):
    name=models.CharField(max_length=50,blank=False)
    price=models.PositiveIntegerField(blank=False)
    stock=models.IntegerField(blank=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    picture = models.ImageField(blank=False, upload_to="pictures/%Y/%m/%d")
    pic_content=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        ordering =('name',)
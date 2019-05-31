from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Store(models.Model):
    objects=models.Manager()
    name=models.CharField(max_length=20)
    num=models.CharField(max_length=20)
    content=models.TextField()
    owner=models.ForeignKey(User,editable=False,on_delete=models.CASCADE,default='1')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('store:detail',args=[str(self.pk)])


class Macarons(models.Model):
    name=models.CharField(max_length=50)
    price=models.PositiveIntegerField()
    stock=models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, upload_to="pictures/%Y/%m/%d")
    pic_content=models.TextField(default='')

    def __str__(self):
        return self.name
    class Meta:
        ordering =('name',)
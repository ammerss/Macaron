from django.db import models
from django.urls import reverse

# Create your models here.
class Store(models.Model):
    objects=models.Manager()
    name=models.CharField(max_length=20)
    num=models.CharField(max_length=20)
    content=models.TextField()
    

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('store:detail',args=[str(self.pk)])
        
   

from django.db import models

# Create your models here.

class Macarons(models.Model):
    name=models.CharField(max_length=50)
    price=models.PositiveIntegerField()
    stock=models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        ordering =('name',)
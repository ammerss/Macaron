from django.db import models
from decimal import Decimal

# Create your models here.
class Review(models.Model):
    #store = models.ForeignKey(Store, on_delete = models.CASCADE)
    writer = models.CharField(max_length = 100, default='')
    post_date = models.DateTimeField(auto_now_add = True)
    title = models.TextField(primary_key = True, max_length = 50, help_text = 'Title of review')
    content = models.TextField(max_length = 500, help_text = 'Content of review')
    rate = models.DecimalField(max_digits = 10, decimal_places = 1, default=Decimal())
    hit = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.title

    def update_hit(self):
        self.hit = self.hit + 1
        self.save()
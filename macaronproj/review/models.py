from django.db import models

# Create your models here.
class Review(models.Model):
    #store = models.ForeignKey(Store, on_delete = models.CASCADE)
    #writer = models.CharField(max_length = 100)
    post_date = models.DateTimeField(auto_now_add = True)
    title = models.TextField(max_length = 50, help_text = '제목을 입력해주세요.')
    content = models.TextField(max_length = 500, help_text = '내용을 입력해주세요.')
    
    def __str__(self):
        return self.title
from django.db import models

class Blog(models.Model):

 # id = 1, 2, 3, 4
  content = models.CharField(max_length=140)
  #auto_now_add 一度だけ保存
  posted_date = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-posted_date']
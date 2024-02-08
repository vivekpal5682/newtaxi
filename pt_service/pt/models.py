from django.db import models

# Create your models here.

class information(models.Model):
    name = models.CharField(max_length=100 , default="" , null = True , blank = True)
    pick = models.CharField(max_length=100 , default ="" , null = True , blank = True)
    drop = models.CharField(max_length=100 , default ="" , null = True , blank = True)
    number = models.IntegerField(max_length = 10 , default ="" , null = True , blank = True)
    # name = models.CharField(max_length = 100 , defalut ="" , null = True , blank = True)
    def __str__(self):
        return str(self.name)

    

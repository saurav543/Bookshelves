from django.db import models


# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=30)
    # picture= models.ImageField()
    auther=models.CharField(max_length=30,default="anonymous")
    discribe=models.TextField(default="django uploaded file")
    file=models.FileField(upload_to='')
    
    def __str__(self):
        return self.name


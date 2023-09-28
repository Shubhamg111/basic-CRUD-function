from django.db import models

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=100,null=False)
    address=models.CharField(max_length=100)
   
    def __str__(self):
       return self.name
   
class Teacher(models.Model):
    name=models.CharField(max_length=100,null=False)
    address=models.CharField(max_length=100)
   
    def __str__(self):
       return self.name
   
from django.db import models

# Create your models here.
class students_details(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=30)
    saddress=models.CharField(max_length=200)
   
    

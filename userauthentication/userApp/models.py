from django.db import models

class user(models.Model):
    username=models.CharField(max_length=50,blank=False,null=False)
    password=models.CharField(max_length=50,blank=False,null=False)
    confirmpassword=models.CharField(max_length=50,blank=False,null=False)

# def __str__(self):
#     return self.username


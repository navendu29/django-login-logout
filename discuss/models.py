from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=250)
    password=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    phone=models.CharField(max_length=10)


    def __str__(self):
          return self.name+'-'+self.password+'-'+self.email+'-'+self.email


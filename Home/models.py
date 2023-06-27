from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    roll=models.CharField(max_length=200)
    semester=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    vote=models.CharField(max_length=200)

    def __str__(self):
        return self.name
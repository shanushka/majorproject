from django.db import models

# Create your models here.
class MyMobileModel(models.Model):
    idd=models.IntegerField()
    namee = models.CharField(max_length=100)
    dimension=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    screen_size=models.CharField(max_length=100)
    resolution=models.CharField(max_length=100)
    os=models.CharField(max_length=100)
    cpu=models.CharField(max_length=100)
    storagee=models.CharField(max_length=100)
    ram=models.CharField(max_length=100)
    front_cam=models.CharField(max_length=100)
    rear_cam=models.CharField(max_length=100)
    wifi=models.CharField(max_length=100)
    battery=models.CharField(max_length=100,default="2200",null=True)
    bluetooth=models.CharField(max_length=100)
    image=models.CharField(max_length=100)
    loudspeaker=models.CharField(max_length=100)

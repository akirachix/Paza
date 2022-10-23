from django.db import models

# Create your models here.
class Resident(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=240,null=True)
    username=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=30,null=True)
    COUNTY_CHOICES=(
       ("N", "Nairobi"),
       ("M", "Mombasa"),
       ("T","Turkana"),
       ("K","Kitale"),
   )
    county=models.CharField(max_length=20,choices=COUNTY_CHOICES,null=True)
    neighbourhood_associattion=models.CharField(max_length=40,null=True)




class Leader(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=240)
    county=models.CharField(max_length=20)
    password=models.CharField(max_length=30,null=True)
    neighbourhood_associattion=models.CharField(max_length=40,null=True)
    username=models.CharField(max_length=30,null=True)



class Notification(models.Model):
    neighbourhood=models.CharField(max_length=20)
    date_of_meeting=models.DateTimeField(null=True)
    tittle_of_meeting=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    date_and_time=models.DateTimeField(null=True)

class Posts(models.Model):
    tittle=models.TextField(max_length=250,null=True) 
    description=models.TextField(max_length=250, null=True) 
    sector=models.TextField(max_length=30, null=True)
    image = models.ImageField(null=True)
    video = models.FileField(null=True)
    time_date = models.DateTimeField(null=True)

# class Comment(models.Model):
#     head=models.TextField(max_length=50,null=True) 
#     # description=models.TextField(max_length=250, null=True) 
    # sector=models.TextField(max_length=30, null=True)
    # image = models.ImageField(null=True)
    # video = models.FileField(null=True)
    # time_date = models.DateTimeField(null=True)    


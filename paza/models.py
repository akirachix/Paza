from trace import Trace
from django.db import models
from cloudinary.models import CloudinaryField

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
    neighbourhood=models.CharField(max_length=20,null=True)
    date_of_meeting=models.DateTimeField(null=True)
    tittle_of_meeting=models.CharField(max_length=20)
    status=models.CharField(max_length=20,null=True)
    date_and_time=models.DateTimeField(null=True)


class Posts(models.Model):
    image = CloudinaryField(null=True)
    image_name = models.CharField(max_length = 100,null=True)
    image_caption = models.TextField(max_length = 500,null=True)
    created = models.DateTimeField(auto_now_add = True,null=True)
    author = models.ForeignKey(Resident, on_delete = models.CASCADE,null=True)
    likes = models.IntegerField(null = True, default = 0)

    def __str__(self):
        return self.image_name

    def delete(self):
        self.delete()

class Comment(models.Model):
    body = models.TextField(null=True)
    created = models.DateTimeField(null=True)
    post = models.ForeignKey('Posts', on_delete = models.CASCADE,null=True)
    author = models.ForeignKey(Resident, on_delete = models.CASCADE,null=True)

    def __str__(self):
        return self.post

class NewPost(models.Model):
    image = CloudinaryField('image') 


class Forum(models.Model):
    tittle=models.CharField(max_length=20) 
    name=models.CharField(max_length=200,null=True )
    topic= models.CharField(max_length=300,null=True)
    description = models.CharField(max_length=1000,blank=True,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.topic)


class Discussion(models.Model):
    forum = models.ForeignKey(Forum,blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.forum)




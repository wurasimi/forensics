from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    items_setchoices=[
        ('AC','AirCondition'),
        ('AIR','Installation'),
        ('FRIGDE','Refridgerator'),
        ('GENERAL','General Servicing'),
    ]
    
    image = models.ImageField(upload_to='post_image', null=True)
    title = models.CharField(max_length=100) 
    content = models.TextField(max_length=2000)
    price = models.IntegerField(blank=True, default=1)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

     
class item(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title
    
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gmail = models.EmailField()
    phone_number = models.CharField(max_length=11)
    enquiry = models.TextField()
    
    def __str__(self):
        return self.first_name
    
    
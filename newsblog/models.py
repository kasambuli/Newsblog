from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt
# Create your models here.
class Profile(models.Model):
    '''
    function to create user profile once user is logged in
    '''
    user = models.OneToOneField(User,related_name = 'profile', null = True)
    avatar = models.ImageField(upload_to = 'avatar/',blank = True)
    bio = models.TextField(max_length=300, null = True)
    email = models.EmailField(blank = True)
    def __str__(self):
        return self.user.username

    # Create Profile when creating a User
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

class News(models.Model):
    '''
    function to add a news article
    '''
    user = models.OneToOneField(User,related_name = 'news', null = True)
    image = models.ImageField(upload_to = 'avatar/',blank = True)
    title = models.CharField(null = True,max_length = 100)
    news = models.TextField(max_length =500, null = True)
    posted = models.DateTimeField(auto_now_add=True,blank = True)

class Comments(models.Model):
    '''
    function to add comments to a particular news article
    '''
    user = models.OneToOneField(User,related_name = 'comment', null = True)
    news = models.ForeignKey(News,null = True)
    comment = models.TextField(max_length =500, null = True)
    posted = models.DateTimeField(auto_now_add=True,blank = True)

 
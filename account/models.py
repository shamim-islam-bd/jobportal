
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


        
# # lets us explicitly set upload path and filename
# def upload_to(instance, filename):
#     return 'images/{filename}'.format(filename=filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    resume = models.FileField(upload_to='resume/', null=True)
    
    
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    user = instance 
    
    if created:
        profile = UserProfile(user=user)
        profile.save()
        
        

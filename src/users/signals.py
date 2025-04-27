from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


# post_save is a signal that is sent after a model's save() method is called
# receiver is a decorator that connects the signal to the function
# any time a User(sender or model instance)  is created, the create_user_profile function will be called
# instance is the user instance that was created, 
# created is a boolean that tells us if the user was created or updated
# kwargs is a dictionary that contains any additional keyword arguments that were passed to the save() method
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        #create a profile instance for the user, then asociate 
        #the profile with the user instance
        Profile.objects.create(user=instance)
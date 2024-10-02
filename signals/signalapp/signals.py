from django.db.models.signals import post_save
from django.dispatch import receiver
from signalapp.models import User

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    # print("reached")
   if created:
      print('A new user was created:', instance.name, instance.email)
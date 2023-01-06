from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from .models import *


@receiver(post_save , sender=User)
def create(sender , created , instance ,**kwargs):
    if created:
        group=Group.objects.get(name='customers')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email,
        )
        # Profile.objects.create(user=instance)
        print('Customer Created')
        print('User added to Group Customers')

 
# post_save.connect(create , sender=User)


# @receiver(post_save , sender=User)
# def update_profile(sender , instance , created , **kwargs):
#     if created == False:
#         instance.profile.save()
#         print('Profile Updated')

# post_save.connect(update_profile , sender=User)
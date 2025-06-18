from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Product(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
    


# When user account will be created auth token 
# will be created and assigned to this user.
@receiver(post_save, sender=User)
def generate_auth_token(sender, instance=None, created=False, **kwargs):

    # If User object has been created.
    if created:

        Token.objects.create(user=instance)
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

@receiver(post_save,sender=User)
def create_auth_t(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(User=instance)



class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    #date = models.DateField()
    def __str__(self):
        return f"{self.movie}"


class Guest(models.Model):
    name = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE )
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE )
    def __str__(self):
        return f"{self.guest} - {self.movie}"


class Post(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    body= models.TextField()

    def __str__(self):
        return self.title



from django.db import models

# Create your models here.

class Song(models.Model):
    url = models.CharField(max_length=500)
    volume = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    seek = models.CharField(max_length=30)
    play = models.CharField(max_length=2)
    mute = models.CharField(max_length=2)
    dj = models.CharField(max_length=30) 

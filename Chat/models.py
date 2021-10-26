from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    mail = models.EmailField()
    passwd = models.CharField(max_length=150)
    photo = models.ImageField()
    hashid = models.CharField(max_length=150, default='')
    
    def __str__(self):
        return self.mail
    
    
class Contects(models.Model):
    you = models.CharField(max_length=150)
    contect = models.CharField(max_length=150)
    
    
class Message(models.Model):
    sender = models.CharField(max_length=150)
    reciever = models.CharField(max_length=150)
    message = models.CharField(max_length=10000)
    
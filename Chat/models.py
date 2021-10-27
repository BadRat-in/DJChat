from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    mail = models.EmailField()
    passwd = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='static\media')
    hashid = models.CharField(max_length=150)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.mail
    


    
class Message(models.Model):
    sender = models.CharField(max_length=150)
    reciever = models.CharField(max_length=150)
    message = models.CharField(max_length=10000)
    isSeen = models.IntegerField(default=0)
    isDeliver = models.IntegerField(default=0)
    time = models.TimeField()
    
    def __str__(self):
        return self.sender + "=>" + self.reciever
    
    
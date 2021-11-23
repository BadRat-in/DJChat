from django.db import models
import hashlib, datetime
from django.utils import timezone

Time = datetime.datetime.now()
time = ""

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    mail = models.EmailField()
    passwd = models.CharField(max_length=512)
    photo = models.ImageField()
    hashid = models.CharField(max_length=512)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.mail
    
def time():
    global time
    if (Time.strftime("%H") > '12'):
        time = Time.strftime("%H:%M AM")
    else:
        temp = int(Time.strftime("%H"))
        temp = temp - 12
        time = Time.strftime(f"{temp}%M PM")

    
class Message(models.Model):
    global target_datetime
    sender = models.CharField(max_length=512)
    reciever = models.CharField(max_length=512)
    message = models.CharField(max_length=10000)
    isSeen = models.IntegerField(default=0)
    isDeliver = models.IntegerField(default=0)
    time = models.TimeField(default=time)
    date = models.DateField(default=Time.strftime("%Y-%m-%d"))
    hashid = models.CharField(max_length=512, null=True)
    def __str__(self):
        return self.hashid
    
    
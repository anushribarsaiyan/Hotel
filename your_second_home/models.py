from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hotels(models.Model):
    name = models.CharField(max_length=30,default=" your_second_home")
    owner = models.CharField(max_length=20)
    location = models.CharField(max_length=10)
    state = models.CharField(max_length=50, default="Gwalior")
    country =models.CharField(max_length=50, default='india')

    def __str__(self):
        return self.name
    

class Rooms(models.Model):
    ROOM_STATUS = (
            ('1',"available"),
            ('2','not_available'),
        )

    ROOM_TYPE = (
            ("1","permium"),
            ("2","deluxe"),
            ("3","basic"),
        )

    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    Capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    status = models.CharField(choices = ROOM_STATUS, max_length = 15)
    room_number = models.IntegerField()

    def __str__(self):
        return self.hotel.name
    

class Reservations(models.Model):
    check_in = models.DateField(auto_now = False)
    check_out = models.DateField()
    room = models.ForeignKey(Rooms, on_delete= models.CASCADE)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)
    booking_id = models.CharField(max_length=100, default="null")

    def __str__(self):
        return self.guest.username


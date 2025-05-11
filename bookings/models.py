from django.db import models
from django.contrib.auth.models import User

class Bus(models.Model):
    name= models.CharField(max_length=100)
    number= models.CharField(max_length=20, unique=True)
    origin= models.CharField(max_length=100)
    destination= models.CharField(max_length=100)
    features= models.TextField()
    start_time= models.TimeField()
    reach_time= models.TimeField()
    no_of_seats= models.PositiveIntegerField() 
    price= models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.number}) - {self.origin} to {self.destination}"

class Seat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Seat {self.seat_number} on {self.bus.name} ({self.bus.number})"
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.bus.name} ({self.seat.seat_number})"
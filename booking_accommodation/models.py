# models.py

from django.db import models
from django.contrib.auth.models import User

class Accommodation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    max_guests = models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} booking at {self.accommodation.name}"

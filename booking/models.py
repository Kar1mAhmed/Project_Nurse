from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.



class Booking(models.Model):
    nurse = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='nurse_bookings')
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient_bookings')
    appointment = models.DateTimeField(default= datetime(2024, 4, 18, 9, 0))
    price = models.DecimalField(max_digits=10, decimal_places=2)

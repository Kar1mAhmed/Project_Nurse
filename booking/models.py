from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from users.models import Nurse, Patient

# Create your models here.



class Booking(models.Model):
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='nurse_bookings')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_bookings')
    appointment = models.DateTimeField(default=datetime(24, 10, 3, 10, 55))
    price = models.DecimalField(max_digits=10, decimal_places=2)

from django.urls import path
from .views import create_booking, list_bookings

urlpatterns = [
    path('api/bookings/create/', create_booking, name='create_booking'),
    path('api/bookings/list/', list_bookings, name='list_bookings'),
]
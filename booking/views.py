from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer



@api_view(['POST'])
def create_booking(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
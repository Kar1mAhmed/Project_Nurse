# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
# from django.urls import reverse_lazy
# from django.http import JsonResponse



# class CustomPasswordResetView(PasswordResetView):
#     success_url = reverse_lazy('password_reset_done')
#     email_template_name = 'registration/password_reset_email.html'
#     subject_template_name = 'registration/password_reset_subject.txt'

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         if self.request.is_ajax():
#             return JsonResponse({"status": "success"})
#         return response



# class CustomPasswordResetConfirmView(PasswordResetConfirmView):
#     success_url = reverse_lazy('password_reset_complete')

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         if self.request.is_ajax():
#             return JsonResponse({"status": "success"})
#         return response








#Reset_Password

# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.auth.models import User
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import PasswordResetSerializer, PasswordResetConfirmSerializer
# from django.utils import timezone
# from django.db import models




# class PasswordResetRequestAPIView(APIView):
#     def post(self, request):
#         serializer = PasswordResetSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             user = User.objects.filter(email=email).first()
#             if user:
#                 # Generate password reset token
#                 uid = urlsafe_base64_encode(force_bytes(user.pk))
#                 token = default_token_generator.make_token(user)

#                 # Send password reset email
#                 reset_url = f"{request.scheme}://{request.get_host()}/api/password_reset/confirm/{uid}/{token}/"
#                 # You should send the reset URL to the user's email here
#                 # For example, using Django's built-in email sending functionality

#                 return Response({'detail': 'Password reset email sent. Please check your email.'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'error': 'No user with that email address.'}, status=status.HTTP_404_NOT_FOUND)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PasswordResetConfirmAPIView(APIView):
#     def post(self, request, uidb64, token):
#         serializer = PasswordResetConfirmSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 uid = force_text(urlsafe_base64_decode(uidb64))
#                 user = User.objects.get(pk=uid)
#             except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#                 user = None

#             if user is not None and default_token_generator.check_token(user, token):
#                 new_password = serializer.validated_data['new_password']
#                 user.set_password(new_password)
#                 user.save()
#                 return Response({'detail': 'Password reset successful.'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'error': 'Invalid reset link.'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import OTP
# from .serializers import OTPSerializer
# import random

# @api_view(['POST'])
# def generate_otp(request):
#     serializer = OTPSerializer(data=request.data)
#     if serializer.is_valid():
#         email = serializer.validated_data['email']
#         otp = ''.join(random.choices('0123456789', k=6))  # Generate OTP
#         OTP.objects.create(email=email, otp=otp)  # Save OTP to database
#         send_mail(
#             'Password Reset OTP',
#             f'Your OTP for password reset is: {otp}',
#             settings.EMAIL_HOST_USER,
#             [email],
#             fail_silently=False,
#         )
#         return Response({'message': 'OTP sent successfully'})
#     else:
#         return Response(serializer.errors, status=400)

# @api_view(['POST'])
# def verify_otp(request):
#     serializer = OTPSerializer(data=request.data)
#     if serializer.is_valid():
#         email = serializer.validated_data['email']
#         otp_entered = serializer.validated_data['otp']
#         otp_obj = OTP.objects.filter(email=email, otp=otp_entered).first()
#         if otp_obj:
#             # If OTP is valid, allow password reset
#             # Implement your password reset logic here
#             otp_obj.delete()  # Delete OTP record from database
#             return Response({'message': 'OTP verified successfully'})
#         else:
#             return Response({'error': 'Invalid OTP'}, status=400)
#     else:
#         return Response(serializer.errors, status=400)


# views.py

#set_pass_OTP

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import OTP
import random

@api_view(['POST'])
def generate_otp(request):
    email = request.data.get('email')
    if email:
        otp = ''.join(random.choices('0123456789', k=6))  # Generate OTP
        OTP.objects.create(email=email, otp=otp)  # Save OTP to database
        send_mail(
            'Password Reset OTP',
            f'Your OTP for password reset is: {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return Response({'message': 'OTP sent successfully'})
    else:
        return Response({'error': 'Email is required'}, status=400)

@api_view(['POST'])
def verify_otp(request):
    email = request.data.get('email')
    otp_entered = request.data.get('otp')
    if email and otp_entered:
        otp_obj = OTP.objects.filter(email=email, otp=otp_entered).first()
        if otp_obj:
            # If OTP is valid, allow password reset
            # Implement your password reset logic here
            otp_obj.delete()  # Delete OTP record from database
            return Response({'message': 'OTP verified successfully'})
        else:
            return Response({'error': 'Invalid OTP'}, status=400)
    else:
        return Response({'error': 'Email and OTP are required'}, status=400)



# views.py
# reset_password
# important

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
# from .models import OTP

# @api_view(['POST'])
# def set_password(request):
#     email = request.data.get('email')
#     password = request.data.get('password')
#     otp_entered = request.data.get('otp')

#     if email and password and otp_entered:
#         otp_obj = OTP.objects.filter(email=email, otp=otp_entered).first()
#         if otp_obj:
#             # If OTP is valid, allow password reset
#             user = User.objects.filter(email=email).first()
#             if user:
#                 user.set_password(password)
#                 user.save()
#                 otp_obj.delete()  # Delete OTP record from database
#                 return Response({'message': 'Password has been reset successfully'})
#             else:
#                 return Response({'error': 'User not found'}, status=404)
#         else:
#             return Response({'error': 'Invalid OTP'}, status=400)
#     else:
#         return Response({'error': 'Email, password, and OTP are required'}, status=400)




from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def reset_password(request):
    if request.method == 'POST':
        email = request.data.get('email')
        new_password = request.data.get('new_password')

        # Retrieve the user by email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        # Update the user's password
        user.password = make_password(new_password)
        user.save()

        return Response({'message': 'Password reset successfully'})

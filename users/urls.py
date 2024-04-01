from django.urls import path, include

from .views import *

# from .views import CustomPasswordResetView, CustomPasswordResetConfirmView



urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    # path('registration/', CustomRegisterView.as_view()),
    path('registration/', include('dj_rest_auth.registration.urls')),
    
    # path('delete/', delete_account),
    # path('reset-password/', reset_password),

    # path('api/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    # path('api/password_reset_confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
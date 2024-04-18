from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.db import models








class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ]


class User(AbstractUser):
    username = models.CharField(max_length=11)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    gender =models.CharField(max_length=20, choices=GENDER_CHOICES)

    national_id = models.CharField(max_length=14)

    national_id_image = models.ImageField(upload_to="images/" , null=True, blank=True)
    selfie = models.ImageField(upload_to="D:\project-main\src\images", null=True, blank=True)
    certificate = models.ImageField(upload_to="D:\project-main\src\images", null=True, blank=True)

    notification_token = models.CharField(max_length=255, null=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email



#2nd_User 

class BasicUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True, blank=True)
    dete_of_birth = models.DateField(default="yy/mm/dd")
    
    

    def __str__(self):
        return self.user.email



class Meta:
    db_table = 'basic_user'
  






class OTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"OTP for {self.email}"

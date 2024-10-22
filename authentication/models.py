from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class AccountManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)
    
class Account(AbstractBaseUser):
    phone_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=256,verbose_name="ism")
    last_name = models.CharField(max_length=256, blank=True, null=True, verbose_name="familya")
    profile_info = models.TextField(blank=True, null=True,verbose_name="o'zingiz haqingizda")
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ["first_name",]

    objects = AccountManager()

    def __str__(self):
        return f"{self.first_name}ning hisobi | {self.phone_number}"
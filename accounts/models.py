from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

    
class CustomUser(AbstractUser):
    phone = PhoneNumberField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)
    username = models.CharField(max_length=150, unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    


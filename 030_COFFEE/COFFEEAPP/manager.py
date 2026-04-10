from COFFEEAPP.models import *
from django.contrib.auth.models import BaseUserManager

class CustomeManager(BaseUserManager):
    def create_user(self, phone, email , password = None, **extra_fields):
        if not phone:
            raise ValueError('phone number is required')
        
        if not email:
            raise ValueError('email is required')
        
        user=self.model(phone=phone,email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, phone, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)

        return self.create_user(phone,email,password,**extra_fields)
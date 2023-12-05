from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _



# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_('Please enter an email address'))

        email=self.normalize_email(email)

        new_user=self.model(email=email,**extra_fields)

        new_user.set_password(password)

        new_user.save()

        return new_user


    def create_superuser(self,email,password,**extra_fields):

        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('Type', 'ADMIN')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))


        return self.create_user(email,password,**extra_fields)
    



class User(AbstractUser):
    USER_TYPE = [
        ("UNSPECIFIED", "Unspecified"),
        ("ADMIN", "Admin"),
        ("EMPLOYEE", "Employee"),
        ("CLIENT", "Client"),
    ]
    Type = models.CharField(max_length=80, choices=USER_TYPE, blank=False, null=False,
                            default="UNSPECIFIED")
    dateEnrolled=models.DateField(auto_now_add=True,null=True,blank=True)
    password_reset_token = models.CharField(max_length=50, null=True, blank=True)
    password_reset_OTP = models.CharField(max_length=50, null=True, blank=True)

    REQUIRED_FIELDS=['email','first_name', 'last_name']
    

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}"



class Employee(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.DateField(null=True,blank = True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    github = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255, null=True,blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='Profile/Employee',null=True,blank=True)


    def __str__(self) -> str:
        return self.user.email
    


class Client(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.DateField(null=True,blank=True)
    phone = models.CharField(max_length=255,null=True,blank=True)
    github = models.CharField(max_length=255, null=True,blank=True)
    linkedin = models.CharField(max_length=255, null=True,blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='Profile/Client',null=True,blank=True)

    def __str__(self) -> str:
        return self.user.email
    

class Admin(models.Model):


    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.DateField(null=True,blank=True)
    phone = models.CharField(max_length=255,null=True,blank=True)
    github = models.CharField(max_length=255, null=True,blank=True)
    linkedin = models.CharField(max_length=255, null=True,blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='Profile/Client/',null=True,blank=True)
    def __str__(self) -> str:
        return self.user.email
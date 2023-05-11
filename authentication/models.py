from django.db import models
from django.contrib.auth.admin import User
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    profile_pic =CloudinaryField('profile image', null=True, blank=True)

    def __str__(self):
        return self.user.username

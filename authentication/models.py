from django.db import models
from django.contrib.auth.admin import User
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.user.username

from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    IMG_STD_SIZE = 300


    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    

    def crop(self, img):
        width, height = img.size   # Get dimensions
        min_size = min(width, height)
        left = max((width - min_size)/2, 0)
        top = max((height - min_size)/2, 0)
        right = max((width + min_size)/2, 0)
        bottom = max((height + min_size)/2, 0)
        # Crop the center of the image
        return img.crop((left, top, right, bottom))
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize
        img = Image.open(self.image.path)
        if (img.height > Profile.IMG_STD_SIZE or img.width > Profile.IMG_STD_SIZE):
            img = self.crop(img)
            img.thumbnail((Profile.IMG_STD_SIZE, Profile.IMG_STD_SIZE))
            img.save(self.image.path)

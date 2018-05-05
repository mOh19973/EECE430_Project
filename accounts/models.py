from django.contrib.auth.models import User
from django.db import models


class ProfilePhoto(models.Model):
    userImg= models.ImageField(upload_to='media', default='media/default-img.png')
    userPhoto = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return 'Photo of ' + self.userPhoto.username

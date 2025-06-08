from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', default='profiles/default.png')
    phone_number = models.CharField(max_length=16, unique=True, blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.phone_number}'

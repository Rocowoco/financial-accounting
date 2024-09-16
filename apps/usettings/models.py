from django.db import models
from django.conf import settings

class UserSettings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    currency = models.CharField(max_length=10, default='USD')
    language = models.CharField(max_length=10, default='en')
    dark_mode = models.BooleanField(default=False)

    def __str__(self):
        return f"Настройки {self.user.username}"

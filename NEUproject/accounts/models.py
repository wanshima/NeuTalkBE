from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    # Add custom fields here, if needed

    def __str__(self):
        return self.username
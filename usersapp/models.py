from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4())
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday = models.DateField(blank=True)
    

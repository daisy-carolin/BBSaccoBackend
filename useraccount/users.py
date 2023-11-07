from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
class User(AbstractUser):
    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
    )
    ROLE=(
        ('Admin','Admin'),
        ('Agente','Agente'),
        ('Managers','Managers'),
    )
    gender=models.CharField(max_length=50,choices=GENDER,blank=False,null=False)
    phone=models.CharField(max_length=15,blank=False,null=False)
    role=models.CharField(max_length=20,choices=ROLE,blank=False,null=False)
    address=models.TextField()
    notes=models.TextField()

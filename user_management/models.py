from django.db import models

from django.contrib.auth.models import AbstractUser

class user_profile(AbstractUser):
    phone_number = models.CharField(default=None,null=True)
    profession = models.CharField(default=None,null=True)
    description = models.CharField(default=None,null=True)
    address = models.CharField(default=None,null=True)
    profile_image = models.FileField(upload_to='user-image/',default=None,null=True)
    status = models.CharField(default='Inactive',null=True)

    class Meta:
        db_table = 'auth_user'
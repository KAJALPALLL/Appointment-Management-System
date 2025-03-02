from django.db import models
from user_management.models import user_profile


class Business_History(models.Model):
    business_man = models.ForeignKey(user_profile,on_delete=models.CASCADE,default=None,null=True)
    status = models.CharField(default="Inactive",null=True)
    start_datetime = models.DateTimeField(default=None,null=True)
    end_datetime = models.DateTimeField(default=None,null=True)


class BookAppointment(models.Model):
    business_man = models.ForeignKey(user_profile,on_delete=models.CASCADE,default=None,null=True)
    customer = models.ForeignKey(user_profile,on_delete=models.CASCADE,default=None,null=True,related_name='xyz')
    datetime = models.DateTimeField(default=None,null=True)
    status = models.CharField(default=None,null=True)


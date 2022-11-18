from django.db import models
from django.contirb.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

# user model
class User(AbstractUser):
    is_doctor= models.BooleanField(default=False)
    is_patient= models.BooleanField(default=False)
    is_admin= models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.is_patient = True
    # patient verification/uniqueness
    pid = models.AutoField(unique=True, primary_key=True)

class Doctor(models.Model):
    # unique physician identification number
    upin = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.is_doctor= True
    expertise = models.CharField(max_length=20)
    days_available = models.DateTimeField(null=True)

class Admin(models.Model):
    aid= models.AutoField(unique=True, primary_key=True)
    post= models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# now create and save the user
# create
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_patient:
            Patient.objects.create(user=instance)
        elif instance.is_doctor:
            Doctor.objects.create(user=instance)
        elif instance.is_admin:
            Admin.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_patient:
        instance.patient.save()
    elif instance.is_doctor:
        instance.doctor.save()
    elif instance.is_admin:
        instance.admin.save()
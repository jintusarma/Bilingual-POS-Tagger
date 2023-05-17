from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_token = models.CharField(max_length=120)
    is_verified = models.BooleanField(default=False)

types = (
    ('verfier_1','VERIFIER_1'),
    ('verfier_2','VERIFIER_2'),
    ('admin','Admin'),
)

class Verifier(models.Model):
    verifier = models.ForeignKey(User, on_delete=models.CASCADE)
    # ver = models.ForeignKey(Profile, on_delete=models.CASCADE)
    verifier_type = models.CharField(max_length=20, choices=types, default= 'verifier1')
    
    
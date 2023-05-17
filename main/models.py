from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dataset(models.Model):
    raw_sentence = models.CharField(max_length=1000,)
    tagged_sentence = models.CharField(max_length=1000)
    verified_sentence = models.CharField(max_length=1000)
    is_default_tagged = models.BooleanField(default=False,verbose_name="Is Tagged By Admin")
    is_tagged = models.BooleanField(default=False,verbose_name="Is Tagged By User")
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.raw_sentence


class TaggerDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tagged_sentence = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


class VerfierDetails(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    verified_sentence = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.verified_sentence
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Verifier
from django.contrib.postgres.fields import ArrayField
# from .models import MetaData

# Create your models here.

class Tagset(models.Model):
    tagset_name = models.CharField("Name of the Tagset", max_length=1000,blank=True, null=True)
    tagset_description = models.CharField(max_length=1000,blank=True, null=True)
    tagset_values = models.CharField(max_length=1000,blank=True, null=True)

    def __str__(self):
        return self.tagset_name

class MetaData(models.Model):
    language = models.CharField(max_length=1000,blank=True, null=True)
    domain = models.CharField(max_length=1000,blank=True, null=True)
    name = models.CharField("Name of the Batch",max_length=1000,blank=True, null=True)  
    tagset = models.ForeignKey(Tagset, on_delete=models.CASCADE,blank=True, null=True) 

    def __str__(self):
        return self.name

class BodoDataset(models.Model):
    raw_sentence = models.CharField(max_length=1000,blank=True, null=True)
    tagged_sentence = models.CharField(max_length=1000,blank=True, null=True)
    verified_sentence = models.CharField(max_length=1000,blank=True, null=True)
    metadata = models.ForeignKey(MetaData, on_delete=models.CASCADE,blank=True, null=True)
    is_default_tagged = models.BooleanField(default=False,verbose_name="Is Tagged By Admin")
    is_tagged = models.BooleanField(default=False,verbose_name="Is Tagged By User")
    is_verified = models.BooleanField(default=False)
    tagger = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True)
    verifier = models.ForeignKey(Verifier, on_delete=models.SET_NULL,blank=True, null=True)
    tagged_at = models.DateTimeField("Tagged At",blank=True, null=True)
    verified_at = models.DateTimeField("Updated At",blank=True, null=True)    

    def __str__(self):
        return self.raw_sentence

class AssameseDataset(models.Model):
    raw_sentence = models.CharField(max_length=1000,blank=True, null=True)
    tagged_sentence = models.CharField(max_length=1000,blank=True, null=True)
    verified_sentence = models.CharField(max_length=1000,blank=True, null=True)
    metadata = models.ForeignKey(MetaData, on_delete=models.CASCADE,blank=True, null=True)
    is_default_tagged = models.BooleanField(default=False,verbose_name="Is Tagged By Admin")
    is_tagged = models.BooleanField(default=False,verbose_name="Is Tagged By User")
    is_verified = models.BooleanField(default=False)
    tagger = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True)
    verifier = models.ForeignKey(Verifier, on_delete=models.SET_NULL,blank=True, null=True)
    tagged_at = models.DateTimeField("Tagged At",blank=True, null=True)
    verified_at = models.DateTimeField("Updated At",blank=True, null=True)    

    def __str__(self):
        return self.raw_sentence


# class TaggerDetails(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     tagged_sentence = models.ForeignKey(BodoDataset, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now=True)


# class VerfierDetails(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     verified_sentence = models.ForeignKey(Dataset, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.verified_sentence

# class MetaData(models.Model):
#     # data = models.ForeignKey(Dataset,on_delete=models.CASCADE)
#     language = models.CharField(max_length=1000,)
#     domain = models.CharField(max_length=1000,)
#     name = models.CharField("Name of the Batch",max_length=1000,)

#     def __str__(self):
#         return self.name

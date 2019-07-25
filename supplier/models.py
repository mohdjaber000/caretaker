from django.db import models
from osm.models import Bussiness, BussinessBranch
# Create your models here.

class Supplier(models.Model):

    name = models.CharField(max_length=256,null=True)
    email = models.EmailField(blank=True)
    phone_primary = models.CharField(max_length=16,blank=True)
    phone_secondary = models.CharField(max_length=16,blank=True)
    address = models.CharField(blank=True, max_length=100)
    country = models.CharField(blank=True, max_length=100)
    region = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=100)
    ghpgps = models.CharField(blank=True, max_length=16)
    comment = models.TextField(blank=True)
    bussiness = models.OneToOneField(Bussiness, on_delete=models.CASCADE, null=True)
    branch = models.OneToOneField(BussinessBranch, on_delete=models.CASCADE, null=True)

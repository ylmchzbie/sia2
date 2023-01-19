from django.db import models

# Create your models here.

class tools_inventory(models.Model):
    item_name = models.CharField(max_length=255)
    item_quantity = models.IntegerField()
    item_type = models.CharField(max_length=255, default=" ")
    
class customer_details(models.Model):
    customerName = models.CharField(max_length=255)
    customerAddress = models.CharField(max_length=255)
    customerEmail = models.CharField(max_length=255)
    customerPhone = models.CharField(max_length=255)
    customerStatus = models.BooleanField()
    
class technician_details(models.Model):
    techName = models.CharField(max_length=255)
    techPhone = models.CharField(max_length=255)
    techEmail = models.CharField(max_length=255)
    techSched = models.CharField(max_length=255)

class supplier_details(models.Model):
    suppName = models.CharField(max_length=255)
    suppAddress = models.CharField(max_length=255)
    suppEmail = models.CharField(max_length=255)
    suppPhone = models.CharField(max_length=255)
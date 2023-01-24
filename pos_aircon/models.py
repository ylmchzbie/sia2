from django.db import models

# Create your models here.

# items
class tools_inventory(models.Model):
    item_name = models.CharField(max_length=255)
    item_quantity = models.IntegerField()
    item_type = models.CharField(max_length=255, default=" ")
    item_price = models.FloatField(default=0)
    
# customer details
class customer_details(models.Model):
    customerName = models.CharField(max_length=255)
    customerAddress = models.CharField(max_length=255)
    customerEmail = models.CharField(max_length=255)
    customerPhone = models.CharField(max_length=255)
    customerStatus = models.BooleanField(default=True)

    
# techinician
class technician_details(models.Model):
    techName = models.CharField(max_length=255)
    techPhone = models.CharField(max_length=255)
    techEmail = models.CharField(max_length=255)
    techSched = models.CharField(max_length=255)

# supplier
class supplier_details(models.Model):
    suppName = models.CharField(max_length=255)
    suppAddress = models.CharField(max_length=255)
    suppEmail = models.CharField(max_length=255)
    suppPhone = models.CharField(max_length=255)


### payment methods
### PAYMENT_MODES = (
###     ('Cash', 'Cash'),
###     ('Credit', 'Credit'),
### )


### class sales_order(models.Model):
###     customer = models.ForeignKey(customer_details, on_delete=models.CASCADE)
###     item = models.ForeignKey(tools_inventory, on_delete=models.CASCADE)
###     dateOrdered = models.DateField(auto_now_add=True)
###     paymentMethod = models.CharField(max_length=10, null=True, choices=PAYMENT_MODES)

###    


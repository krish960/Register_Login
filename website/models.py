from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField(unique=True)
    customer_mobile = models.CharField(max_length=15)
    customer_password = models.CharField(max_length=255)  
    first_name = models.CharField(max_length=15,null=True)
    last_name = models.CharField(max_length=15,null=True)
    Organization = models.CharField(max_length=15,null=True)
    

    def __str__(self):
        return self.customer_name


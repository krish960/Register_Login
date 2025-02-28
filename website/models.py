from django.db import models

# Create your models here.
class Customer(models.Model):
	customer_name=models.CharField(max_length=100)
	customer_mobile=models.CharField(max_length=15)
	customer_email=models.CharField(max_length=15)
	customer_password=models.CharField(max_length=15)
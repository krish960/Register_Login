from django.contrib import admin

# Register your models here.
from website import models
# Register your models here.

# admin.site.register(models.TaskType)

class CustomerAdmin(admin.ModelAdmin):
	list_display=("customer_name","customer_mobile","customer_email","customer_password")
admin.site.register(models.Customer,CustomerAdmin)
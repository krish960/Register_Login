from django.contrib import admin
from django.db.models import Count
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_email', 'customer_mobile', 'first_name', 'last_name', 'Organization')  
    search_fields = ('id', 'customer_email')
admin.site.register(Customer, CustomerAdmin)

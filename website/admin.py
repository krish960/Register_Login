from django.contrib import admin
from django.db.models import Count
from django.shortcuts import render
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_email', 'customer_mobile', 'first_name', 'last_name', 'Organization')  
    search_fields = ('id', 'customer_email')

    def changelist_view(self, request, extra_context=None):
    
        org_count = Customer.objects.values('Organization').distinct().count()
        
     
        extra_context = extra_context or {}
        extra_context['org_count'] = org_count
        
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(Customer, CustomerAdmin)

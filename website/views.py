from django.shortcuts import render,redirect
from website import models
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Customer

# Create your views here.

def Register(req):
	return render(req,"Register.html")


def create_account(req):
	customer = models.Customer(
		customer_name=req.POST['customer_name'],
		customer_mobile=req.POST['customer_mobile'],
		customer_email=req.POST['customer_email'],
		customer_password=req.POST['customer_password']
	)
	customer.save()
	return redirect("/login")

def login(req):
	return render(req,"login.html")

def login_process(req):
    customer = models.Customer.objects.filter(
        customer_mobile=req.POST['customer_mobile'],
        customer_password=req.POST['customer_password']
    ).values()

    customer = list(customer)

    if len(customer) == 0:
        return render(req, "login_Failed.html")
    else:
        req.session['customer_id'] = customer[0]['id']
        customer_name = customer[0]['customer_name']
        customer_mobile = customer[0]['customer_mobile']
        customer_password = customer[0]['customer_password']
        
        return render(req, "home.html", {
            "customer_name": customer_name,
            "customer_mobile": customer_mobile,
            "customer_password": customer_password

        })

    return redirect("/home")

def list_Register(req):
    query = list(Customer.objects.all().values())  
    return JsonResponse(query, safe=False)  
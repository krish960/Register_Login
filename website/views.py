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
		customer_password=req.POST['customer_password'],
        first_name=req.POST['first_name'],
        last_name=req.POST['last_name'],
        Organization=req.POST['Organization']

	)
	customer.save()
	return redirect("/home")

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
        req.session['customer_name'] = customer[0]['customer_name']
        req.session['customer_email'] = customer[0]['customer_email']
        req.session['customer_password'] = customer[0]['customer_password']
        req.session['first_name'] = customer[0]['first_name']
        req.session['last_name'] = customer[0]['last_name']
        req.session['Organization'] = customer[0]['Organization']


        return redirect("/home") 

from django.shortcuts import render, redirect
from collections import Counter
from .models import Customer  

def home(req):
    if 'customer_id' not in req.session:  
        return redirect('/login')  

    customer_id = req.session['customer_id']
    customer = Customer.objects.get(id=customer_id) 

    users = Customer.objects.all()

    organization_counts = dict(Counter(user.Organization for user in users))

    context = {
        "users": users,
        "organization_counts": organization_counts
    }
    return render(req, "home.html", context)



def list_Register(req):
    query = list(Customer.objects.all().values())  
    return JsonResponse(query, safe=False)  

def edit_Organization(req):
    edit=models.Customer.objects.get(id=req.GET['id'])
    obj={"edit":edit}
    return render(req,"edit_Organization.html",obj)

def update_file(req):
    update=models.Customer.objects.get(id=req.POST['id'])
    update.customer_name=req.POST['customer_name']
    update.customer_email=req.POST['customer_email']
    update.first_name=req.POST['first_name']
    update.last_name=req.POST['last_name']
    update.Organization=req.POST['Organization']
    update.save()
    return redirect("/home")

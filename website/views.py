from django.shortcuts import render,redirect
from website import models
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Customer
# Create your views here.

def index(req):
    return render(req,"index.html")

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
        Organization=req.POST['Organization'],
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
        return render(req, "login.html")
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
    if 'customer_id' not in req.session:
        return redirect('/login')

    logged_in_user_id = req.session['customer_id']
    user_to_edit = get_object_or_404(Customer, id=req.GET['id'])

    if user_to_edit.id != logged_in_user_id:
        return JsonResponse({"error": "You are not authorized to edit this account"}, status=403)

    return render(req, "edit_Organization.html", {"edit": user_to_edit})

def update_file(req):
    if 'customer_id' not in req.session:
        return redirect('/login')

    logged_in_user_id = req.session['customer_id']
    user_to_update = get_object_or_404(Customer, id=req.POST['id'])

    if user_to_update.id != logged_in_user_id:
        return JsonResponse({"error": "You are not authorized to update this account"}, status=403)

    user_to_update.customer_name = req.POST['customer_name']
    user_to_update.customer_email = req.POST['customer_email']
    user_to_update.first_name = req.POST['first_name']
    user_to_update.last_name = req.POST['last_name']
    user_to_update.Organization = req.POST['Organization']
    user_to_update.save()

    return redirect("/home")
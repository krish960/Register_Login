from django.shortcuts import render
from website import models

# Create your views here.
# def addmin(req):
#     return render(req, "admin/addmin.html")

def dashbord(req):
	return render(req,"admin/dashbord.html")

def Organizations(req):
	data = models.Customer.objects.all()
	obj = {"data": data}
	return render(req,"admin/Organizations.html",obj)
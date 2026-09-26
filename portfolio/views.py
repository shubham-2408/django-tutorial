from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    query = Job.objects.get(comapny = "Shubham")
    return HttpResponse(f"hello {query.name} welcome to landing page")

def home(request):
    return HttpResponse(f"hello welcome to landing page")

@csrf_exempt
def job(request):
    if request.method =="GET":
        
        jobs=Job.objects.all()
        return render(request ,"portfolio/index.html",{"jobs":jobs} )

    if request.method ==  "POST":
        body = request.body.decode('utf-8')
        data = json.loads(body)

        company = data['company']
        description = data['description']

        job =Job(company=company,description = description)
        job.save()
        return HttpResponse (f"{company} added successfully")

    if request.method =='DELETE':
        body = request.body.decode('utf-8')
        data = json.loads(body)
        company= data['company']

        job = Job.objects.filter(company=company).delete()

        return HttpResponse(f"{company} deleted successfully")
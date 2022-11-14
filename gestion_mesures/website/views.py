from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,"website/welcome.html")

def date(request):
    return HttpResponse('this page was served at '+ str(datetime.now()))
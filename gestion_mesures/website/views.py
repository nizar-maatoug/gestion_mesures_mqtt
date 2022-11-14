from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

from website.models import Grandeur,Mesure

# Create your views here.
def welcome(request):
    return render(request,"website/welcome.html",{"num_grandeurs":Grandeur.objects.count()})

def date(request):
    return HttpResponse('this page was served at '+ str(datetime.now()))
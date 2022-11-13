from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to mesures App')

def date(request):
    return HttpResponse('this page was served at '+ str(datetime.now()))
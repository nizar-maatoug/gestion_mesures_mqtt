from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render,get_object_or_404

from website.models import Grandeur,Mesure

# Create your views here.
def welcome(request):
    return render(request,"website/welcome.html",{"num_grandeurs":Grandeur.objects.count()})

def date(request):
    return HttpResponse('this page was served at '+ str(datetime.now()))

def detailGrandeur(request,id):
    grandeur=get_object_or_404(Grandeur,pk=id)
    return render(request,"website/grandeur/grandeur_detail.html",{"grandeur":grandeur})

def listGrandeur(request):
    grandeurs=Grandeur.objects.all()
    return render(request,"website/grandeur/grandeur_list.html",{"grandeurs":grandeurs})

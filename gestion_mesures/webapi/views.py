from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from website.models import Grandeur, Mesure
from .serializers import GrandeurSerializer, MesureSerializer

@api_view(['GET','POST'])
def add_list_grandeur(request):
    if request.method=='GET':
        #get grandeur list
        grandeurs=Grandeur.objects.all()
        serializer=GrandeurSerializer(grandeurs,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        #add grandeur
        serializer=GrandeurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)




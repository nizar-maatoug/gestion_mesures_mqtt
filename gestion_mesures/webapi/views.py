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

@api_view(['GET','PUT','DELETE'])
def get_modif_delete_grandeur(request,pk):
    #récupérer la grandeur
    try:
        grandeur=Grandeur.objects.get(pk=pk)
    except Grandeur.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=GrandeurSerializer(grandeur)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=GrandeurSerializer(grandeur, request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        grandeur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






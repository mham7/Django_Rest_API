from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

from .serializers import CardSerializer
from .models import card
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def card_list(request,format=None):
    if request.method=='GET':
        cards_list=card.objects.all()
        serializer=CardSerializer(cards_list,many=True)
        return JsonResponse({'drinks':serializer.data},safe=False)
    
    if request.method=='POST':
        serializer=CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def card_view_details(request,id,format=None):
    try:
        Card=card.objects.get(pk=id)
    except card.DoesNotExist:
        return status.HTTP_404_NOT_FOUND
    if request.method=='GET':
        serializer=CardSerializer(Card)
        return Response(serializer.data)
    elif request.method=='PUT':
         serializer=CardSerializer(Card,request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        Card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

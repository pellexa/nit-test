# from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Counterparty
from .serializers import CounterpartySerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_counterparty(request, id):
    try:
        counterparty = Counterparty.objects.get(id=id)
    except Counterparty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single counterparty
    if request.method == 'GET':
        serializer = CounterpartySerializer(counterparty)
        return Response(serializer.data)
    # update details of a single counterparty
    elif request.method == 'PUT':
        serializer = CounterpartySerializer(counterparty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete a single counterparty
    elif request.method == 'DELETE':
        counterparty.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def get_post_counterparties(request):
    # get all counterparties
    if request.method == 'GET':
        counterparties = Counterparty.objects.all()
        serializer = CounterpartySerializer(counterparties, many=True)
        return Response(serializer.data)
    # insert a new record for a counterparty
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'rating': request.data.get('rating'),
        }
        serializer = CounterpartySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

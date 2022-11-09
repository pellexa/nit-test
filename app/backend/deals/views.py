from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Deal
from .serializers import DealSerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_deal(request, id):
    try:
        deal = Deal.objects.get(id=id)
    except Deal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single deal
    if request.method == 'GET':
        serializer = DealSerializer(deal)
        return Response(serializer.data)
    # update details of a single deal
    elif request.method == 'PUT':
        serializer = DealSerializer(deal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete a single deal
    elif request.method == 'DELETE':
        deal.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def get_post_deals(request):
    # get all deals
    if request.method == 'GET':
        deals = Deal.objects.all()
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data)
    # insert a new record for a deal
    elif request.method == 'POST':
        data = {
            'type': request.data.get('type'),
            'dateDeal': request.data.get('dateDeal'),
            'deliveryPoint': request.data.get('deliveryPoint'),
            'volume': request.data.get('volume'),
            'price': request.data.get('price'), 
            'deliveryStart': request.data.get('deliveryStart'),
            'deliveryEnd': request.data.get('deliveryEnd'),
            'tool': request.data.get('tool'),
            'counterparty': request.data.get('counterparty'),
        }
        serializer = DealSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

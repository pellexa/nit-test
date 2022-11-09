from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DeliveryPoint
from .serializers import DeliveryPointSerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_deliveryPoint(request, id):
    try:
        deliveryPoint = DeliveryPoint.objects.get(id=id)
    except DeliveryPoint.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single deliveryPoint
    if request.method == 'GET':
        serializer = DeliveryPointSerializer(deliveryPoint)
        return Response(serializer.data)
    # update details of a single deliveryPoint
    elif request.method == 'PUT':
        serializer = DeliveryPointSerializer(deliveryPoint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete a single deliveryPoint
    elif request.method == 'DELETE':
        deliveryPoint.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def get_post_deliveryPoints(request):
    # get all deliveryPoints
    if request.method == 'GET':
        deliveryPoints = DeliveryPoint.objects.all()
        serializer = DeliveryPointSerializer(deliveryPoints, many=True)
        return Response(serializer.data)
    # insert a new record for a deliveryPoint
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'rating': request.data.get('rating'),
        }
        serializer = DeliveryPointSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

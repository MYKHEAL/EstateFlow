from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import HouseSerializer
from .models import User, House
# Create your views here.

@api_view(['POST'])
def add_house(request):
    serializer = HouseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(User, pk=serializer.validated_data['user'])
    if user.is_resident:
        House.objects.create(
            house_number=serializer.validated_data['house_number'],
            address=serializer.validated_data['address'],
            user=user
        )
        return Response(data={"message": "house added successfully"} ,status=status.HTTP_201_CREATED)

    return Response(data={"message": "Not Authorized"} ,status=status.HTTP_403_FORBIDDEN)
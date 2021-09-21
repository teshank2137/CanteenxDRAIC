from django.shortcuts import render
from django.http import QueryDict

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import CanteenSerializer, CanteenViewSerializer, FoodItemsSerializer, FoodItemsViewSerializer
from . models import Canteens, FoodItems

# Create your views here.


class GetAllCanteens(APIView):
    def get(self, request):
        obj = Canteens.objects.all()
        serializer = CanteenViewSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CanteenSerializer(data=request.data)
        if serializer.is_valid():
            canteenObject = serializer.save()
            # TODO add User to Canteen
            return Response(serializer.data)
        return Response({"error": "Data invalid"}, status=status.HTTP_406_NOT_ACCEPTABLE)


class RegisterFoodItem(APIView):
    def post(self, request):
        serializer = FoodItemsSerializer(data=request.data)
        try:
            canteenId = request.POST['id']
            canteenQuery = Canteens.objects.get(pk=canteenId)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            Item = serializer.save(commit=False)
            Item.canteenId.setValue = canteenQuery
            canteenQuery.menu.add(Item.save())
            return Response(FoodItemsSerializer(data=Item).data)
        return Response({"error": "Data invalid"}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def get(self, request):
        try:
            queryset = FoodItems.objects.all()
            serializer = FoodItemsViewSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)


class UpdateFoodItem(APIView):
    def post(self, request):
        serializer = FoodItemsViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class FoodItemsByCanteenId(APIView):
    def get(self, request, id):
        try:
            queryset = FoodItems.objects.filter(canteen_id=id)
            serializer = FoodItemsSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({'error': 'canteen id not found'}, status=status.HTTP_404_NOT_FOUND)

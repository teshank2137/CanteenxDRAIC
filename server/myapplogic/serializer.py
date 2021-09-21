from rest_framework import serializers
from . models import Canteens, FoodItems


class CanteenViewSerializer(serializers.ModelSerializer):
    class Meta:

        model = Canteens
        fields = ["id", "name", "location", "menu"]


class CanteenSerializer(serializers.ModelSerializer):
    class Meta:

        model = Canteens
        fields = ["name", "location"]


class FoodItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItems
        fields = ["name", "image", "price", "in_stock"]


class FoodItemsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItems
        fields = ["id", "name", "image", "price", "in_stock"]

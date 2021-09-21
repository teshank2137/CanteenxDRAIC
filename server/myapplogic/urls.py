from django.urls import path
from . views import *

urlpatterns = [
    path('all-canteens/', GetAllCanteens.as_view()),
    # path('register-canteen', GetAllCanteens.as_view()),
    path('all-foods/', RegisterFoodItem.as_view()),
    path('update-food-item/', UpdateFoodItem.as_view()),
    path('food-by-canteen-id/<int:id>/', FoodItemsByCanteenId.as_view())
]

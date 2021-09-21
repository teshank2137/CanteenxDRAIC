from django.db import models

# Create your models here.


class FoodItems(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='foodItems/')
    canteen_id = models.ForeignKey(
        "myapplogic.Canteens", on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Canteens(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    menu = models.ManyToManyField(FoodItems)
    # TODO owner_id = models.ForeignKey()

    def __str__(self):
        return self.name

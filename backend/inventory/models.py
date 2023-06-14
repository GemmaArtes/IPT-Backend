from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator

class Category(models.Model):
    type = models.CharField(max_length=500)

    def __str__(self):
        return self.type

class Product(models.Model):
    code=models.IntegerField(validators=[MaxValueValidator(1000)])
    name=models.CharField(max_length=500)
    quantity=models.IntegerField(validators=[MaxValueValidator(1000)])
    price=models.FloatField(validators=[MaxValueValidator(1000)])
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    
    def __str__(self):
        return self.name

class Report(models.Model):
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_add=models.IntegerField(validators=[MaxValueValidator(1000)])
    stockleft=models.IntegerField(validators=[MaxValueValidator(1000)])
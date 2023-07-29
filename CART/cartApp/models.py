from django.db import models

# Create your models here.
class Product(models.Model):
    Item=models.IntegerField()
    product=models.CharField(max_length=30)
    price=models.IntegerField()
    quantity=models.IntegerField()
    
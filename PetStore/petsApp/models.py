from django.db import models

# Create your models here.
class Pet(models.Model):
    gender=(("male","male"),("female","female"))
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    species=models.CharField(max_length=30)
    gender=models.CharField(max_length=30,choices=gender)
    image=models.ImageField(upload_to="media")
    breed=models.CharField(max_length=30)
    description=models.CharField(max_length=100)
    price=models.IntegerField()

class Meta:
    db_table="Pet"
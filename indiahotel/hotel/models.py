from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dish(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.ImageField(upload_to="dish_images",null=True)
    def __str__(self):
        return self.name
    
class DishReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    dish=models.ForeignKey(Dish,on_delete=models.CASCADE,related_name='dish')
    review=models.CharField(max_length=50)
    rating=models.IntegerField()
    date=models.DateField(null=True,auto_now_add=True)
   
    

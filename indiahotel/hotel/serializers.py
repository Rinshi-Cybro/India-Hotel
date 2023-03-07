from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Dish

class DishSerializer(serializers.Serializer):
    name=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()
    

class DishModelSer(serializers.ModelSerializer):
    class Meta:
        model=Dish
        fields="__all__"
    def validate(self, data):
        cost=data.get("price")
        if cost<0:
            raise serializers.ValidationError
        return data
        

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)        
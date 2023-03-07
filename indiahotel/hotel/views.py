from django.shortcuts import render
from rest_framework.views import APIView,Response
from .serializers import DishSerializer,DishModelSer,UserModelSerializer
from rest_framework.viewsets import ViewSet
from rest_framework import status
from .models import Dish


# Create your normal views here.
# class DishView(APIView):
#     def post(self,request,*args,**kwargs):
#         dish=DishSerializer(data=request.data)
#         if dish.is_valid():
#             name=dish.validated_data.get("name")
#             cat=dish.validated_data.get("category")
#             prc=dish.validated_data.get("price")
#             Dish.objects.create(name=name,category=cat,price=prc)
#             return Response({"msg":"ok"})
#         return Response({"msg":"failed"})
#     def get(self,request,*args,**kwargs):
#         if "category" in request.query_params:
#             cat=request.query_params.get("category")
#             dishes=Dish.objects.filter(category=cat)
#             des_dish=DishSerializer(dishes,many=True)
#             return Response(data=des_dish.data)
#         dishes=Dish.objects.all()
#         des_dish=DishSerializer(dishes,many=True)
#         return Response(data=des_dish.data)

# model serializer views
class DishModelView(APIView):
    def post(self,request,*args,**kwargs):
        dish=DishModelSer(data=request.data)
        if dish.is_valid():
            dish.save()
            return Response({"msg":"ok"})
        return Response({"msg":dish.errors},status=status.HTTP_404_NOT_FOUND)
    def get(self,request,*args,**kwargs):
        dish=Dish.objects.all()
        des_dish=DishModelSer(dish,many=True)
        return Response(data=des_dish.data)
    
    
    
# class SpesificdishItem(APIView):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         dish=Dish.objects.get(id=id)
#         des_dish=DishSerializer(dish)
#         return Response(data=des_dish.data)
#     def delete(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         dish=Dish.object.get(id=id)
#         dish.delete()
#         return Response({"msg":"ok"})
#     def put(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         new_dish=DishSerializer(data=request.data)
#         if new_dish.is_valid():
#             old_dish=Dish.objects.get(id=id)
#             old_dish=name=new_dish.validated_data.get("name")
#             old_dish=category=new_dish.validated_data.get("category")
#             old_dish=price=new_dish.validated_data.get("price")
#             old_dish.save()
#             return Response({"msg":"ok"})
#         return Response({"msg":"failed"})



# model serializer views
class DishModelItem(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            dish=Dish.objects.get(id=id)
            des_dish=DishModelSer(dish)
            return Response(data=des_dish.data)
        except:
            return Response({"msg":"Failed"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,*args,**kwargs):
        try:
            id=kwargs.get("id")
            dish=Dish.objects.get(id=id)
            dish.delete()
            return Response({"msg":"ok"})
        except:
            return Response({"msg":"Failed"},status=status.HTTP_404_NOT_FOUND)
    def put(self,request,*args,**kwargs):
        try:
            id=kwargs.get("id")
            old_dish=Dish.objects.get(id=id)
            new_dish=DishModelSer(data=request.data,instance=old_dish)
            if new_dish.is_valid():
                new_dish.save()
                return Response({"msg":"ok"})
            else:
                return Response({"msg":new_dish.errors},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"msg":"Failed"},status=status.HTTP_404_NOT_FOUND)
        
                    
class UserView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            new_user=UserModelSerializer(data=request.data)
            if new_user.is_valid():
                new_user.save()
                return Response({"msg":"ok"})
            else:
                return Response({"msg":new_user.errors},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"msg":"Failed"},status=status.HTTP_404_NOT_FOUND)
        


#views using Viewsets
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import permissions,authentication

class DishViewViewset(ViewSet):
    #items insert chayyan
    def create(self,request,*args,**kwargs):
        dish=DishModelSer(data=request.data)
        if dish.is_valid():
            dish.save()
            return Response({"msg":"ok"})
        return Response({"msg":dish.errors},status=status.HTTP_404_NOT_FOUND)
    
    #coplete items list edukkan
    def list(self,request,*args,**kwargs):
        dish=Dish.objects.all()
        if "category" in request.query_params:
            cat=request.query_params.get("category")
            dish=dish.filter(category=cat)
        if "price_lt" in request.query_params:
            pl=request.query_params.get("price_lt")
            dish=dish.filter(price__lte=pl)    
        des_dish=DishModelSer(dish,many=True)
        return Response(data=des_dish.data)
    
    #spesific items get cheyyan
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        try:
            dish=Dish.objects.get(id=id)
            des_dish=DishModelSer(dish)
            return Response(data=des_dish.data)
        except:
            return Response({"msg":"Failed"},status=status.HTTP_404_NOT_FOUND)
        
    #items edits cheyyan
    def update(self,request,*args,**kwargs):
        try:
            id=kwargs.get("pk")
            old_dish=Dish.objects.get(id=id)
            new_dish=DishModelSer(data=request.data,instance=old_dish)
            if new_dish.is_valid():
                new_dish.save()
                return Response({"msg":"ok"})
            else:
                return Response({"msg":new_dish.errors},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"msg":"Failed"},status=status.HTTP_404_NOT_FOUND)
        
    #items delete cheyyan
    def destroy(self,request,*args,**kwargs):
        try:
            id=kwargs.get("pk")
            dish=Dish.objects.get(id=id)
            dish.delete()
            return Response({"msg":"ok"})
        except:
            return Response({"msg":"Failed"},status=status.HTTP_404_NOT_FOUND) 
         
        

#views using ViewSetView MODEL
#authentication using basic authentication

class DishModelViewSetView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=DishModelSer
    queryset=Dish.objects.all()
    model=Dish
    

# a3ff2da51176b71d1d78b8be8a1b763e7686542e






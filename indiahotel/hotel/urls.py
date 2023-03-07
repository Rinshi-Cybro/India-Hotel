from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('dish',DishModelView.as_view()),
    path('dish/<int:id>',DishModelItem.as_view()),
    path('user',UserView.as_view()),
    path('token',obtain_auth_token),                             
]

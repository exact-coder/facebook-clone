from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .serializers import (UserSerializer,UserCreateSerializer)
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.get_serializer().Meta.model.objects.filter(is_active=True)
            return self.queryset
        else:
            return self.queryset
    def get_object(self):
        return get_object_or_404(self.serializer_class.Meta.model,pk=pk)
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        else:
            return super().get_permissions()
        
    def list(self,request):
        user_serializer = self.serializer_class(self.get_queryset(),many=True)
        return Response(user_serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        user_serializer = UserCreateSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def update(self,request,pk=None):
        user = self.get_object(pk=pk)
        user_serializer = self.serializer_class(user,data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'User updated successfully','data':user_serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        user = self.serializer_class.Meta.model.objects.filter(is_active=True,pk=pk).first()
        if user:
            user_serializer = self.serializer_class(user)
            return Response(user_serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'message':'User not found'},status=status.HTTP_404_NOT_FOUND)
    def destroy(self,request,pk=None):
        user = self.get_object(pk=pk)
        user.is_active = False
        if user.is_active == False:
            user.save()
            return Response({'message':'User deleted successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'User not deleted'},status=status.HTTP_400_BAD_REQUEST)
    
# len 25min
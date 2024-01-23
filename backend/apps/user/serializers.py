from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password','first_name','last_name','bio','image',)

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField(required=True,write_only=True,min_length=5)
    password2 = serializers.CharField(required=True,write_only=True,min_length=5)

    def validate(self,data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Password doesn't match")
        else:
            return data

#===========AUTH==============
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass
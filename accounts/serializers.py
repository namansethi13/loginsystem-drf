from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer): #user serailzer with all the fields
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name' , 'last_name')


class RegisterSerializer(serializers.ModelSerializer): # User serializezr for registration
    confirm_password = serializers.CharField(write_only=True, required=True) #adding additional feild confirm passowrd and making required = True to handle all the errors
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','confirm_password','first_name','last_name')
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
        }

    def create(self, validated_data): #create method for creating a new user
        first_name = validated_data['first_name'] if 'first_name' in validated_data else "" # If first name is passed then it is used else it is set to empty string
        last_name = validated_data['last_name'] if 'last_name' in validated_data else "" # If  last name is passed then it is used else it is set to empty string
        validated_data.pop('confirm_password') # Removing the confirm passed feild as it is not required
        user = User.objects.create_user(
            validated_data['username'].lower(),
            validated_data['email'],
            validated_data['password'],
            first_name = first_name,
            last_name = last_name
        )
        return user


from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics,status, permissions
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import RegisterSerializer, UserSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import TokenAuthentication


specialCharacters = "!@#$%^&*_-+=~`|\/:;,.?"

class RegisterAPI(generics.GenericAPIView): #class based view to register a user
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs): # POST request handling
        serializer = self.get_serializer(data=request.data) # getting data
        serializer.is_valid(raise_exception=True)# Checking if passed data is valid

        # Get the validated data from the serializer
        validated_data = serializer.validated_data
        password = validated_data['password']
        confirm_password = validated_data['confirm_password']
        """

        all password checks:
        """
        if password != confirm_password:
            return Response({"error": "password and confirm password don't match"}, status=status.HTTP_400_BAD_REQUEST)
        if len(password) <8:
             return Response({"error": "password should be greater than 8 characters"}, status=status.HTTP_400_BAD_REQUEST)
        elif(any(char.isalpha() for char in password) == False):
            return Response({"error": "password should contain atleast 1 alphabet"}, status=status.HTTP_400_BAD_REQUEST)
        elif(any(char.isupper() for char in password) == False):
            return Response({"error": "password should contain atleast 1 uppercase letter"}, status=status.HTTP_400_BAD_REQUEST)
        elif(any(char.islower() for char in password) == False):
            return Response({"error": "password should contain atleast 1 lowercase letter"}, status=status.HTTP_400_BAD_REQUEST)
        elif(any(char.isdigit() for char in password) == False):
            return Response({"error": "password should contain atleast 1 digit"}, status=status.HTTP_400_BAD_REQUEST)
        elif all(x not in specialCharacters for x in password):
            return Response({"error": "password should contain atleast 1 special character"}, status=status.HTTP_400_BAD_REQUEST)

        # CREATING USER IF ALL CHECKS ARE PASSED
        user = serializer.create(validated_data=validated_data)
        token = default_token_generator.make_token(user)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1] 
        }) #Returning user and token



class LoginAPI(KnoxLoginView): # Class based login view
    
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        print(request.data)
        request.data['username'] = request.data['username'].lower() #getting username in lowercase
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user) #Logging in user with the details
        return super(LoginAPI, self).post(request, format=None)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def profile(request): # Function based view for getting and updating profile
    if request.method == 'GET': #Get the user
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    if request.method == 'PUT': # Update the user
        user = request.user
        """
        checking if user wants to update username and if username is already in the database
        """
        if 'username' in request.data and User.objects.exclude(pk=user.pk).filter(username=request.data.get('username').lower()).exists():
            return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)

        """
        checking if user wants to update Email and if Email is already in the database
        """
        if 'email' in request.data and User.objects.exclude(pk=user.pk).filter(email__iexact=request.data.get('email')).exists():
            return Response({'error': 'Email already taken'}, status=status.HTTP_400_BAD_REQUEST)
        """
        Updating all the feilds
        """
        user.username = request.data.get('username', user.username).lower()
        user.email = request.data.get('email', user.email)
        user.first_name = request.data.get('first_name', user.first_name)
        user.last_name = request.data.get('last_name', user.last_name)
        user.save()
        return Response({'success': 'updated'})

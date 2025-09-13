from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view ,  permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model, authenticate
from .models import users
from .serialiizer import Userserializer
import re

class Register(generics.CreateAPIView):
    queryset = users.objects.all()
    serializer_class =  Userserializer


class Login_view(generics.GenericAPIView):
    serializer_class =  Userserializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username ,  password=password)
        #vatidate users existence
        if user:
            token ,  created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "username": user.username})
        return Response({"error" : "invalid credentials "},  status=status.HTTP_401_UNAUTHORIZED)
    
User  =  get_user_model()
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    confirm_password =  request.data.get("confirmPassword")

    if not username or not email or not password or not confirm_password:
        return Response({"error": "⚠️ All fields are required"}, status=400)
    
    if password != confirm_password:
        return Response({"password doesnt match"})

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already registered"}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "user": {"username": user.username, "email": user.email}})
    

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = authenticate(request, username=email, password=password)
    if not user:
        return Response({"error": "Invalid credentials"}, status=401)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "user": {"username": user.username, "email": user.email}})
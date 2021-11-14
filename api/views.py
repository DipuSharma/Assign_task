from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User
from .serializers import UserSerializer


class Record(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


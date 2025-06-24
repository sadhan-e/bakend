from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Home(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})

class EchoData(APIView):
    def post(self, request):
        data = request.data
        return Response({"received": data}, status=status.HTTP_200_OK) 
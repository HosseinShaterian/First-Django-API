from django.shortcuts import render
from rest_framework import viewsets
from . models import CustomerRequest
from .serializers import CustomerRequestSerializer

# Create your views here.


class CustomerRequestView(viewsets.ModelViewSet):
    queryset = CustomerRequest.objects.all()
    serializer_class = CustomerRequestSerializer

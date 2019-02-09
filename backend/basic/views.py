from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DataSerializer
from .models import Data

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

# Create your views here.

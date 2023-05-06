from django.shortcuts import render
from rest_framework import viewsets

# import local data
from .serializers import ClienteSerializer
from .models import Cliente

# create a viewset
class ClienteViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = Cliente.objects.all()
	
	# specify serializer to be used
	serializer_class = ClienteSerializer


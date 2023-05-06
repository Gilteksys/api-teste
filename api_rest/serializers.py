# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Cliente

# Create a model serializer
class ClienteSerializer(serializers.ModelSerializer):
	# specify model and fields
	class Meta:
		model = Cliente
		fields = ('__all__')

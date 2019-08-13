from rest_framework import serializers
from .models import Order,OrderDetails

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model=Order
		exclude=('is_active',)

class OrderDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model=OrderDetails
		exclude=('is_active',)

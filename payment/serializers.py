from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Payment
class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Payment
		fields='__all__'
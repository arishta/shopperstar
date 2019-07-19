from rest_framework import serializers
from .models import Category,Subcategory,Products

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=Category
		fields='__all__'

class SubcategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=Subcategory
		fields='__all__'

class ProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model=Products
		fields='__all__'
		

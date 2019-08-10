from rest_framework import serializers
from .models import Category,Subcategory,Products

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=Category
		exclude=('is_active',)

class SubcategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=Subcategory
		exclude=('is_active',)

class ProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model=Products
		exclude=('is_active',)
		

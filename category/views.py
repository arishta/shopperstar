from django.shortcuts import render
from .models import Category,Subcategory,Products
from .serializers import CategorySerializer,SubcategorySerializer,ProductsSerializer
from rest_framework.views import APIView
from django.http import JsonResponse 
from login_signup.token_verification import TokenVerify


class CategoryView(APIView):
	def post(self,request):
		if request.method=='POST':
			category_name=request.query_params['category_name']
			queryset=Category.objects.filter(name=category_name)
			if not queryset:
				category=Category(name=category_name)
				category.save()
				serializer=CategorySerializer(Category.objects.filter(name=category_name),many=True)
				return JsonResponse({"category details":serializer.data})
			else:
				return JsonResponse({"message":"category already exists"})	
	def delete(self,request):
		if request.method=='DELETE':				
			category_id=request.query_params['category_id']
			queryset=Category.objects.filter(id=category_id)
			if queryset:
				queryset.delete()
				return JsonResponse({"message":"category successfully deleted"})
			else:
				return JsonResponse({"message":"category does not exist"})	
	def get(self,request):
		if request.method=='GET':	
			serializer=CategorySerializer(Category.objects.all(),many=True)
			return JsonResponse({"categories":serializer.data})


class SubcategoryView(APIView):
	def post(self,request):
		if request.method=='POST':
			subcategory_name=request.query_params['subcategory_name']
			category_id=request.query_params['category_id']
			queryset=Category.objects.filter(name=subcategory_name).filter(category_id=category_id)
			if not queryset:
				subcategory=Subcategory(name=subcategory_name,category_id=category_id)
				subcategory.save()
				serializer=SubcategorySerializer(Category.objects.filter(name=subcategory_name).filter(category_id=category_id),many=True)
				return JsonResponse({"subcategory details":serializer.data})
			else:
				return JsonResponse({"message":"subcategory already exists in the given category"})	
	def delete(self,request):
		if request.method=='DELETE':				
			subcategory_id=request.query_params['subcategory_id']
			queryset=Subcategory.objects.filter(id=subcategory_id)
			if queryset:
				queryset.delete()
				return JsonResponse({"message":"subcategory successfully deleted"})
			else:
				return JsonResponse({"message":"caetegoy does not exist"})	
	def get(self,request):
		if request.method=='GET':	
			serializer=SubcategorySerializer(Subcategory.objects.all(),many=True)
			return JsonResponse({"subcategories":serializer.data})


class ProductView(APIView):
	def post(self,request):
		if request.method=='POST':
			product_name=request.query_params['product_name']
			category_id=request.query_params['category_id']
			subcategory_id=request.query_params['subcategory_id']
			queryset=Products.objects.filter(name=product_name).filter(category_id=category_id).filter(subcategory_id=subcategory_id)
			if not queryset:
				product=Products(name=product_name,category_id=category_id,subcategory_id=subcategory_id)
				product.save()
				serializer=ProductsSerializer(Products.objects.filter(name=product_name).filter(category_id=category_id).filter(subcategory_id=subcategory_id),many=True)
				return JsonResponse({"product details":serializer.data})
			else:
				return JsonResponse({"message":"product already exists in the given category and subcategory"})
	def delete(self,request):
		if request.method=='DELETE':				
			product_id=request.query_params['product_id']
			queryset=Products.objects.filter(id=product_id)
			if queryset:
				queryset.delete()
				return JsonResponse({"message":"product successfully deleted"})
			else:
				return JsonResponse({"message":"product does not exist"})	
	def get(self,request):
		if request.method=='GET':	
			serializer=ProductsSerializer(Products.objects.all(),many=True)
			return JsonResponse({"subcategories":serializer.data})
			




		

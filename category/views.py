from django.shortcuts import render
from .models import Category,Subcategory,Products
from .serializers import CategorySerializer,SubcategorySerializer,ProductsSerializer
from rest_framework.views import APIView
from django.http import JsonResponse 
from django.db.models import Q
import json



class CategoryView(APIView):
	def post(self,request):
		category_name=request.data.get('category_name')
		queryset=Category.objects.filter(name=category_name,is_active=1)
		if not queryset:
			category=Category(name=category_name)
			category.save()
			serializer=CategorySerializer(Category.objects.filter(name=category_name,is_active=1),many=True)
			return JsonResponse({"message":"category added","category details":serializer.data})
		else:
			return JsonResponse({"message":"category already exists"})
				
	def delete(self,request):				
		category_id=request.data.get('category_id')
		queryset=Category.objects.filter(id=category_id,is_active=1)
		if queryset:
			Category.objects.filter(id=category_id).update(is_active=0)
			return JsonResponse({"message":("category successfully deleted")})
		else:
			return JsonResponse({"message":"category to be deleted not found"})

	def get(self,request):	
		serializer=CategorySerializer(Category.objects.filter(is_active=1),many=True)
		return JsonResponse({"categories":serializer.data})

class SubcategoryView(APIView):	
	def post(self,request):
		subcategory_name=request.data.get('subcategory_name')
		category_id=request.data.get('category_id')
		queryset=Subcategory.objects.filter(name=subcategory_name,category_id=category_id,is_active=1)
		if not queryset:
			subcategory=Subcategory(name=subcategory_name,category_id=category_id)
			subcategory.save()
			serializer=SubcategorySerializer(Subcategory.objects.filter(name=subcategory_name,category_id=category_id,is_active=1),many=True)
			return JsonResponse({"subcategory details":serializer.data})
		else:
			return JsonResponse({"message":"subcategory already exists in the given category"})	
	def delete(self,request):				
		subcategory_id=request.data.get('subcategory_id')
		queryset=Subcategory.objects.filter(id=subcategory_id,is_active=1)
		if queryset:
			Subcategory.objects.filter(id=subcategory_id).update(is_active=0)
			return JsonResponse({"message":"subcategory successfully deleted"})
		else:
			return JsonResponse({"message":"subcategory to be deleted not found"})
	def get(self,request):	
		serializer=SubcategorySerializer(Subcategory.objects.filter(is_active=1),many=True)
		return JsonResponse({"subcategories":serializer.data})

class ProductView(APIView):
	def post(self,request):
		product_name=request.data.get('product_name')
		category_id=request.data.get('category_id')
		subcategory_id=request.data.get('subcategory_id')
		price=request.data.get('price')
		currency=request.data.get('currency')
		quantity_in_stock=request.data.get('quantity_in_stock')
		bogo=request.data.get('bogo')
		queryset=Products.objects.filter(name=product_name,category_id=category_id,subcategory_id=subcategory_id,is_active=1)
		if not queryset:
			product=Products(name=product_name,category_id=category_id,subcategory_id=subcategory_id,price=price,currency=currency,quantity_in_stock=quantity_in_stock,bogo=bogo)
			product.save()
			serializer=ProductsSerializer(Products.objects.filter(name=product_name,category_id=category_id,subcategory_id=subcategory_id,is_active=1).order_by('price'),many=True)
			return JsonResponse({"product details":serializer.data})
		else:
			return JsonResponse({"message":"product already exists in the given category and subcategory"})
	def delete(self,request):				
		product_id=request.data.get('product_id')
		queryset=Products.objects.filter(id=product_id,is_active=1)
		if queryset:
			Products.objects.update(id=product_id,is_active=0)
			return JsonResponse({"message":"product successfully deleted"})
		else:
			return JsonResponse({"message":"product does not exist"})
	
	def get(self,request):
		serializer=ProductsSerializer(Products.objects.filter(is_active=1),many=True)
		return JsonResponse({"message":serializer.data})        	
   

class SearchView(APIView):
	def get(self,request):
		search=request.data.get('search')
		sort=request.data.get('sort')
		filter=request.data.get('filter')
		if filter:
			start,end=request.data.get('filter').split('-')
			q1=Products.objects.filter(is_active=1).filter(Q(name__icontains=search)|
			Q(subcategory__name__icontains=search)| 
			Q(category__name__icontains=search)).filter(price__gte=(start),price__lte=(end))
		else:
			q1=Products.objects.filter(is_active=1).filter(Q(name__icontains=search)|
			Q(subcategory__name__icontains=search)| 
			Q(category__name__icontains=search))

		for row in q1:
			row.view_count+=1
			row.save()
		if sort=="low to high":
			q1=q1.order_by('price','name')	
			serializer=ProductsSerializer(q1,many=True)
			return JsonResponse({"response":serializer.data})
		elif sort=="high to low":
			q1=q1.order_by('-price','name')
			serializer=ProductsSerializer(q1,many=True)
			return JsonResponse({"response":serializer.data})				
		elif sort=="most popular":
			q1=q1.order_by('views')
			serializer=ProductsSerializer(q1,many=True)
			return JsonResponse({"response":serializer.data})



					


			




		

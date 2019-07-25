from django.shortcuts import render
from .models import Category,Subcategory,Products
from .serializers import CategorySerializer,SubcategorySerializer,ProductsSerializer
from rest_framework.views import APIView
from django.http import JsonResponse 
from login_signup.token_verification import TokenVerify
from django.db.models import Q



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
			queryset=Category.objects.filter(name=subcategory_name,category_id=category_id)
			if not queryset:
				subcategory=Subcategory(name=subcategory_name,category_id=category_id)
				subcategory.save()
				serializer=SubcategorySerializer(Category.objects.filter(name=subcategory_name,category_id=category_id),many=True)
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
			queryset=Products.objects.filter(name=product_name,category_id=category_id,subcategory_id=subcategory_id)
			if not queryset:
				product=Products(name=product_name,category_id=category_id,subcategory_id=subcategory_id)
				product.save()
				serializer=ProductsSerializer(Products.objects.filter(name=product_name,category_id=category_id,subcategory_id=subcategory_id.order_by('price')),many=True)
				return JsonResponse({"product details":serializer.data})
			else:
				return JsonResponse({"message":"product already exists in the given category and subcategory"})
	def delete(self,request):
		if request.method=='DELETE':				
			product_id=request.query_params['product_id']
			if queryset:
				queryset.delete()
				return JsonResponse({"message":"product successfully deleted"})
			else:
				return JsonResponse({"message":"product does not exist"})
	
	def get(self,request):
		if request.method=="GET":
			serializer=ProductsSerializer(Products.objects.all(),many=True)
			return JsonResponse({"message":serializer.data})        	
   

class SearchView(APIView):
	def get(self,request):
		if request.method=="GET":
			search=request.query_params['search']
			sort=request.query_params['sort']
			start,end=request.query_params['filter'].split('-')
			q1=Products.objects.filter(Q(name__icontains=search)|
			Q(subcategory__name__icontains=search)| 
			Q(category__name__icontains=search)).filter(price__gte=(start),price__lte=(end))
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
				


			




		

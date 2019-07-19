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
			category=Category(name=category_name)
			category.save()
			serializer=CategorySerializer(Category.objects.filter(name=category_name),many=True)
			return JsonResponse({"category details":serializer.data})
	def delete(self,request):
		if request.method=='DELETE':				
			category_id=request.query_params['category_id']
			queryset=Category.objects.filter(id=category_id)
			if queryset:
				queryset.delete()
				return JsonResponse({"message":"category successfully deleted"})
			else:
				return JsonResponse({"message":"query does not fetch a response"})	
	def get(self,request):
		if request.method=='GET':	
			serializer=CategorySerializer(Category.objects.all(),many=True)
			return JsonResponse({"categories":serializer.data})


class SubcategoryView(APIView):
	def post(self,request):
		if request.method=='POST':
			subcategory_name=request.query_params['subcategory_name']
			category_id=request.query_params['category_id']
			subcategory=Subcategory(name=subcategory_name,category_id=category_id)
			subcategory.save()
			serializer=SubcategorySerializer(Subcategory.objects.filter(name=subcategory_name).filter(category_id=category_id),many=True)
			return JsonResponse({"subcategory details":serializer.data})
	def delete(self,request):
		if request.method=='DELETE':				
			subcategory_id=request.query_params['subcategory_id']
			queryset=Subcategory.objects.filter(id=subcategory_id)
			if queryset:
				queryset.delete()
				return JsonResponse({"message":"subcategory successfully deleted"})
			else:
				return JsonResponse({"message":"query does not fetch any response"})	
	def get(self,request):
		if request.method=='GET':	
			serializer=SubcategorySerializer(Subcategory.objects.all(),many=True)
			return JsonResponse({"subcategories":serializer.data})


		

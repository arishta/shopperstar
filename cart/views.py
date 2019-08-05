from django.shortcuts import render
from .models import Order,OrderDetails
from category.models import Products
from rest_framework.views import APIView
from django.http import JsonResponse 
from django.db.models import Q
from rest_framework.authtoken.models import Token
import json
from django.contrib.auth.models import User
from django.db.models import F

class CartAddView(APIView):
	def post(self,request):
		data=json.loads(request.body)
		data=data['items']
		_,token=request.META.get('HTTP_AUTHORIZATION').split(' ')
		token=Token.objects.get(key=token) 
		user_id=token.user_id
		queryset=Order.objects.filter(user_id=user_id).values('order_id')
		if queryset:
			order_id=queryset[0]['order_id']
		total_amount=0
		for i in data:
			product_id=i['id']
			Quantity=i['quantity']
			quantity_in_stock=Products.objects.filter(id=product_id).values('quantity')
			if quantity_in_stock<Quantity:
				return JsonResponse({"message":"not in stock","available quantity":quantity_in_stock})
			price=Products.objects.filter(id=product_id).values('price')
			price=price[0]['price']
			total_amount+=price*Quantity
			if queryset:
				q=OrderDetails.objects.filter(order_id_id=order_id,product_id=product_id)
				if q:
					OrderDetails.objects.filter(order_id_id=order_id,product_id=product_id).update(quantity=F('quantity')+Quantity)
				else:
					OrderDetails.objects.create(order_id_id=order_id,product_id=product_id,quantity=quantity).values('order_id_id')
			else:
				order_id=Order.objects.create(user_id=user_id).values('order_id')
			Products.objects.filter(id=product_id).update(quantity_in_stock=F('quantity_in_stock')-Quantity)
		price,currency=Order.objects.filter(order_id_id=order_id).update(total=F('total')+total_amount).values('price','currency')
		return JsonResponse({"cart total":str(price)+currency})

class CartRemoveView(APIView):
	def post(self,request):
		data=json.loads(request.body)
		data=data['items']
		_,token=request.META.get('HTTP_AUTHORIZATION').split(' ')
		token=Token.objects.get(key=token) 
		user_id=token.user_id
		queryset=Order.objects.filter(user_id=user_id).values('order_id')
		if queryset:
			order_id=queryset[0]['order_id']
		else:
			return JsonResponse({"message":"user cart is empty"})
		for i in data:
			product_id=i['id']
			quantity=i['quantity']
			q=OrderDetails.objects.filter(order_id_id=order_id,product_id=product_id)
			if q:
				OrderDetails.objects.update(order_id_id=order_id,product_id=product_id,quantity=F('quantity')-quantity)
				price=Products.objects.update(product_id=product_id,quantity_in_stock=F('quantity_in_stock')+quantity).values('price')
				Order.objects.update(order_id=order_id,price=F('price')-total)
			else:
				return JsonResponse({"message":"product not found in cart"})
		total=Order.objects.filter(order_id=order_id).values('total')
		return JsonResponse({"updated cart total":total})

class CartDisplay(APIView):
	def get(self,request):
		_,token=request.META.get('HTTP_AUTHORIZATION').split(' ')
		token=Token.objects.get(key=token) 
		user_id=token.user_id
		queryset=Order.objects.filter(user_id=user_id).values('order_id','total')
		if queryset:
			order_id=queryset[0]['order_id']
			cart_total=queryset[1]['total']
		else:
			return JsonResponse({"message":"user cart is empty"})
		q=OrderDetails.objects.filter(order_id_id=order_id).values('product_id','quantity')
		return JsonResponse({"cart details":q})
		




















		







		return JsonResponse({"mssg":"okay"})

class CartRemoveView(APIView):
	def post(self,request):
		pass







		
			

	




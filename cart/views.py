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
					OrderDetails.objects.filter(order_id_id=order_id,product_id=product_id).update(quantity+=Quantity)
				else:
					OrderDetails.objects.create(order_id_id=order_id,product_id=product_id,quantity=quantity).values('order_id_id')
			else:
				order_id=Order.objects.create(user_id=user_id).values('order_id')
			Products.objects.filter(id=product_id).update(quantity_in_stock-=Quantity)
		price,currency=Order.objects.filter(order_id_id=order_id).update(total+=total_amount).values('price','currency')
		return JsonResponse({"cart total":str(price)+currency})













		







		return JsonResponse({"mssg":"okay"})

class CartRemoveView(APIView):
	def post(self,request):
		pass







		
			

	




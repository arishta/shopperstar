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
from .serializers import OrderDetailsSerializer
from utility import *


class CartAddView(APIView):
	def post(self,request):
		data=json.loads(request.body)
		data=data['items']	
		user_id=get_userid_from_token(request)
		queryset=Order.objects.filter(user_id=user_id,is_active=1).values()
		if queryset:
			order_id=queryset[0]['id']
		else:
			order=Order(id=user_id,user_id=User.objects.get(id=user_id))
			order.save()
			order_id=Order.objects.get(user_id=user_id)
		total_amount=0
		for i in data:
			product_id=i['id']
			Quantity=i['quantity']
			q=Products.objects.filter(id=product_id,is_active=1).values()
			if not q:
				return JsonResponse({"message":"product_id "+str(product_id)+"not found"})
			else:
				quantity_in_stock=q[0]['quantity_in_stock']
			if quantity_in_stock<Quantity:
				return JsonResponse({"message":"not in stock","available quantity":quantity_in_stock})
			price=q[0]['price']
			total_amount+=price*Quantity
			Q=OrderDetails.objects.filter(order_id=order_id,product_id=product_id,is_active=1)
			if Q:
				OrderDetails.objects.filter(order_id=order_id,product_id=product_id,is_active=1).update(quantity=F('quantity')+Quantity)
			else:
				OrderDetails.objects.create(order_id=Order.objects.get(id=order_id),product_id=Products.objects.get(id=product_id),quantity=Quantity)	
			Products.objects.filter(id=product_id).update(quantity_in_stock=F('quantity_in_stock')-Quantity)
		Order.objects.filter(id=order_id,is_active=1).update(total=F('total')+total_amount)
		qset=OrderDetails.objects.filter(order_id=order_id)
		serializer=OrderDetailsSerializer(qset,many=True)
		return JsonResponse({"cart total":serializer.data})

class CartRemoveView(APIView):
	def post(self,request):
		data=json.loads(request.body)
		data=data['items']
		user_id=get_userid_from_token(request)		
		queryset=Order.objects.filter(user_id=user_id,is_active=1).values('id')
		if queryset:
			order_id=queryset[0]['id']
		else:
			return JsonResponse({"message":"user cart is empty"})
		for i in data:
			total=0
			product_id=i['id']
			quantity=i['quantity']
			if not Products.objects.filter(id=product_id,is_active=1):
				return JsonResponse({"message":"product_id "+str(product_id)+" not found"})
			q=OrderDetails.objects.filter(order_id=order_id,product_id=product_id,is_active=1).values('quantity')
			if q:
				q=q[0]['quantity']
				if quantity>q:
					return JsonResponse({"message":"quantity of "+str(product_id)+"greater than in cart"})

				if quantity==q:
					OrderDetails.objects.update(order_id=order_id,product_id=product_id,is_active=0)
				else:
					OrderDetails.objects.update(order_id=order_id,product_id=product_id,quantity=F('quantity')-quantity)

				product=Products.objects.get(id=product_id)
				product.quantity_in_stock=product.quantity_in_stock+quantity
				price=product.price
				product.save()

				total=price*quantity
				Order.objects.update(id=order_id,total=F('total')-total)
			else:
				return JsonResponse({"message":"product not found in cart"})
		qset=OrderDetails.objects.filter(order_id=order_id,is_active=1)
		serializer=OrderDetailsSerializer(qset,many=True)

		return JsonResponse({"updated cart total":serializer.data})

class CartDisplay(APIView):
	def get(self,request):
		user_id=get_userid_from_token(request
			)
		queryset=Order.objects.filter(user_id=user_id,is_active=1).values('id','total')
		if queryset:
			order_id=queryset[0]['id']
			cart_total=queryset[0]['total']
		else:
			return JsonResponse({"message":"user cart is empty"})
		q=OrderDetails.objects.filter(order_id=order_id)
		serializer=OrderDetailsSerializer(q,many=True)
		return JsonResponse({"cart details":serializer.data})
		






		
			

	




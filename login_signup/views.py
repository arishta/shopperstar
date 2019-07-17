from django.shortcuts import render
from django.http import JsonResponse
from .models import UserInfo
from .serializers import UserInfoSerializer
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated  
from django.contrib.auth import authenticate
from uuid import uuid4

class login(APIView):
	permission_classes = (IsAuthenticated,) 
	def get(self,request):
		username=request.GET.get('username')
		password=request.GET.get('password')
		if username and password is not None:
			queryset=UserInfo.objects.filter(Q(username=username)&Q(password=password))
			if queryset:
				rand_token = uuid4()
				UserInfo.objects.filter(username=username).update(token=rand_token)
				return JsonResponse({"status":"true","token":rand_token})
			else:
				return JsonResponse({"status":"false"})	
		else:
			return JsonResponse({"status":"false"})

class signup(APIView):
	def get(self,request):
		first_name=request.GET.get('first_name')
		last_name=request.GET.get('last_name')
		username=request.GET.get('username')
		password=request.GET.get('password')
		queryset=UserInfo.objects.filter(username=username)
		if queryset:
			return JsonResponse({"response":"username already exists"})
		else:	
			user=UserInfo(first_name=first_name,last_name=last_name,username=username,password=password)
			user.save()
			serializer=UserInfoSerializer(UserInfo.objects.filter(username=username),many=True)
			return JsonResponse({"user":serializer.data})	
				
		

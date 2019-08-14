from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import UserInfo
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND,
	HTTP_200_OK
)
from rest_framework.response import Response
from django.contrib.auth import authenticate
from utility import *



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
	username = request.data.get("username")
	password = request.data.get("password")
	if username is None or password is None:
		return JsonResponse({'error': 'Please provide both username and password'})
	user = authenticate(username=username, password=password)
	if not user:
		return JsonResponse({'error': 'Invalid Credentials'})
	token, _ = Token.objects.get_or_create(user=user)
	return JsonResponse({'token': token.key})


@csrf_exempt
@api_view(['GET'])
@permission_classes((AllowAny,))
def signup(request):
	first_name=request.GET.get('first_name')
	last_name=request.GET.get('last_name')
	username=request.GET.get('username')
	password=request.GET.get('password')
	queryset=User.objects.filter(username=username)
	if queryset:
		return JsonResponse({"message":"username already exists"})
	else:	
		user=User(first_name=first_name,last_name=last_name,username=username,password=password)
		user.set_password(user.password)
		user.save()
		return JsonResponse({"message":"signup successful"})

class ProfileView(APIView):
	def get(self,request):
		user_id=get_userid_from_token(request)
		serializer=UserSerializer(User.objects.filter(id=user_id),many=True)
		return JsonResponse({"status":"authorized","user":serializer.data}) 

		
				


		

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




@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    print(username)
    print(password)
    user = authenticate(username=username, password=password)
    print(user)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@permission_classes((AllowAny,))
def signup(request):
	first_name=request.GET.get('first_name')
	last_name=request.GET.get('last_name')
	username=request.GET.get('username')
	password=request.GET.get('password')
	queryset=User.objects.filter(username=username)
	print(queryset)
	if queryset:
		return JsonResponse({"response":"username already exists"})
	else:	
		user=User(first_name=first_name,last_name=last_name,username=username,password=password)
		user.save()
		serializer=UserSerializer(User.objects.filter(username=username),many=True)
		return JsonResponse({"user":serializer.data})

		
				


		

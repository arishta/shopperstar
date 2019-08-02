from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from login_signup.models import UserInfo
from login_signup.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User




class ProfileView(APIView):
	def get(self,request):
			serializer=UserInfoSerializer(UserInfo.objects.all(),many=True)
			return JsonResponse({"status":"authorized","user":serializer.data})	
				

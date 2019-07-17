from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from login_signup.models import UserInfo
from login_signup.serializers import UserInfoSerializer



class ProfileView(APIView):
	def get(self,request):
		token_id=request.headers['token']
		queryset=UserInfo.objects.filter(token=token_id)
		if queryset:
			serializer=UserInfoSerializer(UserInfo.objects.filter(token=token_id),many=True)
			return JsonResponse({"status":"authorized","user":serializer.data})
		else:
			return JsonResponse({"status":"not authorized"})	

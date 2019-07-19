from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from login_signup.models import UserInfo
from login_signup.serializers import UserInfoSerializer
from login_signup.token_verification import TokenVerify



class ProfileView(APIView):
	def get(self,request):
		token_id=TokenVerify(request)
		if token_id:
			serializer=UserInfoSerializer(UserInfo.objects.filter(authorization_token=token_id),many=True)
			return JsonResponse({"status":"authorized","user":serializer.data})	
		else:
			return JsonResponse({"message":"unauthorized access"})		

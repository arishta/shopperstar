from login_signup.models import UserInfo

class token_authorization():
	def verify(self,token):
		queryset= UserInfo.objects.filter(authorization_token=token)
		if queryset:
			return 1
		else:
			return 0	
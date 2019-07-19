from .models import UserInfo

def TokenVerify(request):
	token=request.headers['Authorization']
	query=UserInfo.objects.filter(authorization_token=token)
	if query:
		return token
	else:
		return None
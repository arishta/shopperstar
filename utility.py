from rest_framework.authtoken.models import Token

def get_userid_from_token(request):
	_,token=request.META.get('HTTP_AUTHORIZATION').split(' ')
	token=Token.objects.get(key=token) 
	return token.user_id
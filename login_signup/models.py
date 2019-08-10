from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class UserInfo(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
	country=models.CharField(max_length=10,null=True)	
	class Meta:
		db_table='user'
	
		
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)
	
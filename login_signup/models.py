from django.db import models

class UserInfo(models.Model):
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	authorization_token=models.CharField(max_length=50,null=True)
	def __str__(self):
		return (self.first_name+" "+self.last_name)

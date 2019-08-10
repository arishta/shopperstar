from django.db import models
from django.contrib.auth.models import User
from category.models import Products
class Order(models.Model):
	INR='₹'
	USD='$'
	CURRENCY_LIST=[(INR,'INR'),(USD,'USD')]
	user_id=models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')
	total=models.DecimalField(max_digits=8,decimal_places=2,default=0)
	currency=models.CharField(max_length=4,choices=CURRENCY_LIST,default=INR)
	is_active=models.BooleanField(default=True)

	def __str__(self):
		return str(self.user_id)

class OrderDetails(models.Model):
	class Meta:
		verbose_name_plural='OrderDetails'
	order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
	product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
	quantity=models.IntegerField(default=0)
	is_active=models.BooleanField(default=True)
	def __str__(self):
		return str(self.order_id)
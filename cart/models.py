from django.db import models
from django.contrib.auth.models import User
class Order(models.Model):
	INR='₹'
	USD='$'
	CURRENCY_LIST=[(INR,'INR'),(USD,'USD')]
	user_id=models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')
	order_id=models.IntegerField(primary_key=True)
	total=models.DecimalField(max_digits=8,decimal_places=2,default=True)
	currency=models.CharField(max_length=4,choices=CURRENCY_LIST,default=INR)

	def __str__(self):
		return str(self.total)+self.currency

class OrderDetails(models.Model):
	order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
	product_id=models.IntegerField()
	quantity=models.IntegerField()
	def __str__(self):
		return self.order_id
from django.db import models
from cart.models import Order

class Payment(models.Model):
	INR='₹'
	USD='$'
	CURRENCY_LIST=[(INR,'INR'),(USD,'USD')]
	order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
	amount_paid=models.DecimalField(max_digits=8,decimal_places=2)
	currency=models.CharField(max_length=3,choices=CURRENCY_LIST,default=INR)
	def __str__(self):
		return str(self.amount_paid)+self.currency

	
	
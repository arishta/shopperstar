from django.db import models



class Category(models.Model):
	name=models.CharField(max_length=30)
	class Meta:
		db_table='Category'
		verbose_name_plural='categories'
	def __str__(self):
		return self.name

class Subcategory(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	name=models.CharField(max_length=30)
	class Meta:
		db_table='Subcategory'
		verbose_name_plural='subcategories'
	def __str__(self):
		return self.name

class Products(models.Model):
	INR='₹'
	USD='$'
	CURRENCY_LIST=[(INR,'INR'),(USD,'USD')]
	subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	name=models.CharField(max_length=50)
	price=models.DecimalField(max_digits=8,decimal_places=2,db_column='price')
	currency=models.CharField(max_length=3,choices=CURRENCY_LIST,default=INR,db_column='currency')
	view_count=models.IntegerField(default=0)
	@property
	def combined(self):
		return self.price+self.currency
	
	class Meta:
		db_table='Products'
		verbose_name_plural='products'
	def __str__(self):
		return self.name	
from django.db import models

class Category(models.Model):
	name=models.CharField(max_length=30)
	class Meta:
		db_table='Category'
	def __str__(self):
		return self.name

class Subcategory(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	name=models.CharField(max_length=30)
	class Meta:
		db_table='Subcategory'
	def __str__(self):
		return self.name

class Products(models.Model):
	subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
	category=models.ForeignKey(Category,default='',on_delete=models.CASCADE)
	name=models.CharField(max_length=30)
	class Meta:
		db_table='Products'
	def __str__(self):
		return self.name	